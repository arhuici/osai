# Ángel Romero Huici

import unittest
from unittest.mock import patch, mock_open

from scripts.s_wordcloud import get_abstract, draw_wordcloud

class TestWordcloud(unittest.TestCase):

    """
    Testing get_abstract()
    """
    @patch("requests.post")
    def test_get_abstract_success(self, mock_post):
        """ Test get_abstract() with a valid Grobid response """

        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <front>
                    <abstract>This is an abstract</abstract>
                </front>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            abstract = get_abstract("dummy.pdf")

        self.assertEqual(abstract, "This is an abstract")


    @patch("requests.post")
    def test_get_abstract_multiple_abstracts(self, mock_post):
        """ Test get_abstract() with a valid Grobid response """

        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <front>
                    <abstract>This is an abstract</abstract>
                    <abstract>This is another abstract</abstract>
                </front>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            abstract = get_abstract("dummy.pdf")

        self.assertEqual(abstract, "This is an abstract")


    @patch("requests.post")
    def test_get_abstract_no_abstract(self, mock_post):
        """ Test get_abstract() when no abstract is found in XML """
        
        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <front></front>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            abstract = get_abstract("dummy.pdf")

        self.assertEqual(abstract, "")


    @patch("requests.post")
    def test_get_abstract_request_fail(self, mock_post):
        """ Test get_abstract() when Grobid returns an error """
        
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            abstract = get_abstract("dummy.pdf")

        self.assertEqual(abstract, "")


    """
    Testing draw_wordcloud()
    """
    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_draw_wordcloud(self, mock_show, mock_savefig):
        """ Test draw_wordcloud() saves the image correctly """
        
        abstracts = ["This is a test abstract", "Another abstract with words"]
        draw_wordcloud(abstracts)

        mock_savefig.assert_called_with("persistent/results/wordcloud.png")


    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_draw_wordcloud_no_abstracts(self, mock_show, mock_savefig):
        """ Test draw_wordcloud()  when no data is found """
        
        abstracts = ["",""]

        with patch("builtins.print") as mock_print:
            draw_wordcloud(abstracts)
            mock_print.assert_called_with("No abstracts found")


if __name__ == "__main__":
    unittest.main()
