import unittest
from culturalheritage.toolbox.artifact import Artifact

class TestArtifact (unittest.TestCase):
    def setUp(self):
        self.artifact = Artifact()
        print("Hello")

    def test_sum(self):
        self.assertEqual(self.artifact.sum(1,2),3)