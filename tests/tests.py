import json

from django.conf import settings
from django.test import Client, RequestFactory, TestCase
from tests.models import House, Owner

from rest_framework_discovery.views import DiscoveryViewsets


class TestViews(TestCase):
    """Basic integration testing for generated API functionality."""

    def setUp(self):
        self.client = Client()
        Owner.objects.create(first_name="John", last_name="Smith")

    def tearDown(self):
        Owner.objects.all().delete()

    def test_get_request(self):
        """Perform GET request on the generated viewset."""
        response = self.client.get('/api/tests_owner/')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        """Perform POST request on the generated viewset."""
        response = self.client.post(
            '/api/tests_owner/',
            json.dumps({'owner_id': 2, 'first_name': 'Jane', 'last_name': 'Appleseed'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)

    def test_put_request(self):
        """Perform PUT request on the generated viewset."""
        response = self.client.post(
            '/api/tests_owner/1/',
            json.dumps({'owner_id': 1, 'first_name': 'Jim', 'last_name': 'Smith'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 405)  # TODO: Method not allowed for now.

    def test_patch_request(self):
        """Perform PATCH request on the generated viewset."""
        response = self.client.patch(
            '/api/tests_owner/1/',
            json.dumps({'first_name': 'Johnny'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_request(self):
        """Perform DELETE request on the generated viewset."""
        response = self.client.delete('/api/tests_owner/1/')
        self.assertEqual(response.status_code, 204)


class TestReadOnlyViews(TestCase):
    """
    When the read-only setting is enabled, PUT/PATCH/POST and DELETE
    methods are not available.
    """

    def setUp(self):
        settings.DISCOVERY_READ_ONLY = True
        owner = Owner.objects.create(first_name="John", last_name="Smith")
        House.objects.create(owner=owner, property_name='123 Test', country='CA')
        self.viewsets = {tbl: vs for tbl, vs in [i for i in DiscoveryViewsets().get_viewsets()] if 'test' in tbl}
        self.factory = RequestFactory()

    def tearDown(self):
        settings.DISCOVERY_READ_ONLY = False
        House.objects.all().delete()

    def test_get_request(self):
        """Perform GET request on the generated viewset."""
        for table_name, viewset_class in self.viewsets.items():
            request = self.factory.get('/api/' + table_name)
            response = viewset_class.as_view({'get': 'retrieve'})(request, pk=1)
            self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        """Perform POST request on the generated viewset."""
        request = self.factory.post(
            '/api/tests_owner/',
            {'owner_id': 2, 'first_name': 'Jane', 'last_name': 'Appleseed'}
        )
        with self.assertRaises(AttributeError):
            # Object should have no attribute 'create' in read-only.
            self.viewsets['tests_owner'].as_view({'post': 'create'})(request, pk=2)

    def test_put_request(self):
        """Perform PUT request on the generated viewset."""
        request = self.factory.put(
            '/api/tests_owner/1/',
            {'owner_id': 1, 'first_name': 'Jim', 'last_name': 'Smith'}
        )
        with self.assertRaises(AttributeError):
            # Object should have no attribute 'update' in read-only.
            self.viewsets['tests_owner'].as_view({'put': 'update'})(request, pk=1)

    def test_patch_request(self):
        """Perform PATCH request on the generated viewset."""
        request = self.factory.patch('/api/tests_owner/1/', {'first_name': 'Johnny'})
        with self.assertRaises(AttributeError):
            # Object should have no attribute 'partial_update' in read-only.
            self.viewsets['tests_owner'].as_view({'patch': 'partial_update'})(request, pk=1)

    def test_delete_request(self):
        """Perform DELETE request on the generated viewset."""
        request = self.factory.delete('/api/tests_owner/1/')
        with self.assertRaises(AttributeError):
            # Object should have no attribute 'destroy' in read-only.
            self.viewsets['tests_owner'].as_view({'delete': 'destroy'})(request, pk=1)


class TestExcludeTable(TestCase):
    """
    Using the DISCOVERY_EXCLUDE setting, we avoid generation
    of viewsets for the items in the list.
    """

    def setUp(self):
        settings.DISCOVERY_EXCLUDE = ['tests_house']
        self.viewsets = {tbl: vs for tbl, vs in [i for i in DiscoveryViewsets().get_viewsets()] if 'test' in tbl}

    def test_get_request(self):
        self.assertTrue(self.viewsets['tests_owner'])
        self.assertRaises(KeyError, lambda: self.viewsets['tests_house'])


class TestIncludeTable(TestCase):
    """
    Using the DISCOVERY_INCLUDE setting, we only generate
    viewsets for the items in the list.
    """

    def setUp(self):
        settings.DISCOVERY_INCLUDE = ['tests_owner']
        self.viewsets = [i for i in DiscoveryViewsets().get_viewsets()]

    def test_get_request(self):
        self.assertEqual(len(self.viewsets), 1)
