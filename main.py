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

text_header = "<h1>Enter some text to ROT13:</h1>"

form = """
<form action="/" method="post">
    <label>
        Rotate by:
        <input name="rot_num"/ value="%(rot_num)s">
        <br>
        <br>
    <label>
        Text:
        <input textarea name="added_text" value="%(added_text)s" cols="80" rows="10"></textarea>
    <br>
    <br>
    <input type="submit">
</form>
"""

page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    """Handles requests coming in to "/"
    """

    def write_form(self, added_text="", rot_num=""):
        main_content = text_header + form % {"added_text": added_text,
                                             "rot_num": rot_num}
        response = page_header + main_content + page_footer
        self.response.write(response)

    def get(self):
        self.write_form()

    def post(self):
        new_text = self.request.get("added_text")
        rotation = self.request.get("rot_num")
        rotation = int(rotation)
        newText = ""
        for char in new_text:
            newChar = rotate_character(char, rotation)
            newText = newText + newChar

        self.write_form(newText, rotation)

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
], debug=True)
