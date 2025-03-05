# Ángel Romero Huici

import unittest
from unittest.mock import patch, mock_open

from scripts.s_links import get_links

class TestLinks(unittest.TestCase):

    """
    Testing get_links()
    """
    @patch("requests.post")
    def test_get_links_success(self, mock_post):
        """ Test get_links() when there are links """

        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <p>Referencias: https://example.com y http://test.com</p>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            links = get_links("dummy.pdf")

        self.assertEqual(links, ["https://example.com", "http://test.com"])


    @patch("requests.post")
    def test_get_links_no_links(self, mock_post):
        """ Test get_links() when there are no links """
        
        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <p>Este es un documento sin enlaces.</p>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            links = get_links("dummy.pdf")

        self.assertEqual(links, [])


    @patch("requests.post")
    def test_get_links_request_fail(self, mock_post):
        """ Test get_links() when Grobid returns an error """
        
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            links = get_links("dummy.pdf")

        self.assertEqual(links, [])


if __name__ == "__main__":
    unittest.main()
