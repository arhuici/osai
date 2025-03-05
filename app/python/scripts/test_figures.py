# Ángel Romero Huici

import unittest
from unittest.mock import patch, mock_open

from scripts.s_figures import get_n_figures, draw_figures

class TestFigures(unittest.TestCase):

    """
    Testing get_n_figures()
    """
    @patch("requests.post")
    def test_get_n_figures_success(self, mock_post):
        """ Test get_n_figures() when there are figures """

        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <figure>Figura 1</figure>
                <figure>Figura 2</figure>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            num_figures = get_n_figures("dummy.pdf")

        self.assertEqual(num_figures, 2)


    @patch("requests.post")
    def test_get_n_figures_no_figures(self, mock_post):
        """ Test get_n_figures() when there are no figures """
        
        xml_response = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
            </text>
        </TEI>"""
        
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = xml_response

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            num_figures = get_n_figures("dummy.pdf")

        self.assertEqual(num_figures, 0)


    @patch("requests.post")
    def test_get_n_figures_request_fail(self, mock_post):
        """ Test get_n_figures() when Grobid returns an error """
        
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        with patch("builtins.open", mock_open(read_data=b"%PDF-1.4")):
            num_figures = get_n_figures("dummy.pdf")

        self.assertEqual(num_figures, 0)


    """
    Testing draw_figures()
    """
    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_draw_figures(self, mock_show, mock_savefig):
        """ Test draw_figures() saves the image correctly """
        
        figures = [1, 3, 5, 2]
        draw_figures(figures)

        mock_savefig.assert_called_with("persistent/results/figures.png")


    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_draw_figures_no_figures(self, mock_show, mock_savefig):
        """ Test draw_figures() saves the image correctly """
        
        figures = []
        draw_figures(figures)

        mock_savefig.assert_called_with("persistent/results/figures.png")


if __name__ == "__main__":
    unittest.main()
