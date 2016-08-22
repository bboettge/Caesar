import webapp2
import cgi
from helpers import alphabet_position, rotate_character

#html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>ROT13</title>
    <style type="text/css">
    </style>
</head>
<body>
"""

#html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
    """Handles requests coming in to "/"
    """

    def get(self):

        text_header = "<h1>Enter some text to ROT13:</h1>"

        #form for adding text
        add_form = """
        <form action="/add" method="post">
            <textarea name="added_text" cols="80" rows="10"></textarea>
            <br>
            <input type="submit">
        </form>
        """

        main_content = text_header + add_form
        response = page_header + main_content + page_footer
        self.response.write(response)

class rot_13(webapp2.RequestHandler):
    """Handles requests coming in to '/add'
    """

    def post(self):
        new_text = self.request.get("added_text")

        newText = ""
        for char in new_text:
            newChar = rotate_character(char, 13)
            newText = newText + newChar


        self.response.write(newText)

#    def alphabet_position(letter):
#    """returns position (0-25) of a letter
#    """
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    letter = letter.lower()
#    value = alphabet.index(letter)
#    return value
#





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', rot_13)
], debug=True)
