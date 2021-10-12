class Translation(object):

      
      START_TEXT = """
Hi {},
I am auto Captions Bot with custom markdown and Dynamic support created by @AJPyroVerse.
➪ Remember, Promote me as admin in your channel before any attempting any further steps.
"""    
      DYNAMIC_TEXT = """
  <u>About Dynamic</u>
  You can add {variable_name} in caption, bot will replace these variables by its value according to file.
  Example: Title: {filename}
  Supported variables:
  filename, ext
  Additional variables:
  For video files: width, height
  For audio files: title, artist
"""


      MARKDOWN_TEXT = """
🔰 <u>𝐀𝐛𝐨𝐮𝐭 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧</u>
👉 <b>Bold text</b>
      
📌 <code>**text**</code>
👉 <b>Italic text</b>
📌 <code>__text__</code>
👉 <b>Underline text</b>
      
📌 <code>--text--</code>
👉 <b>Strike text</b>
📌 <code>~~text~~</code>
👉 <b>Code text</b>
📌 <code>`text`</code>
👉 <b>Hyperlink text</b>
📌 <code>[text](https://t.me/durov)</code>
"""
