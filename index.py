#!python
print("content-type: text/html; charset=utf-8\n")
print()
print('''<!doctype html>
<html>
<head>
<title>WEB1 - HTML</title>
<meta charset="utf-8">

<link rel="stylesheet" href="style.css">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
      <input type="button" value="night" onclick="
      nightDayHandler(this);
    ">
<ol>
<li><a href="1.html">HTML</a></li>
<li><a href="2.HTML">CSS</a></li>
<li><a href="3.html">JavaScript</a></li>
</ol>
<div id="article">
<h2>HTML</h2>
<p><a href="http://www.w3.org/TR/html5/" target="_blank" title="html5 specfication">Hypertext Markup Language(HTML)</a> is the standard markup language for <strong>documents designed</strong> to be displayed <u>in a web browser</u>
Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages.</p> <p>HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.
HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as directly introduce content into the page. Other tags such as surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.</p></div></div>
<img src="coding.jpg" width="550">
<p>HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. <br>Inclusion of CSS defines the look and layout of content.<br> The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.</p></body>
')
''')
