import mechanize
import BeautifulSoup as bs

search_query = raw_input("Input the book to be searched for:")

# Browser
br = mechanize.Browser()


# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_gzip(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = 'http://junglee.com/'
r = br.open(url)

#i=0
#for f in br.forms():
#  i = i +1
#	print str(i) 
#	print f


br.select_form(nr=0)
br.form['field-keywords']=search_query
br.submit()
html = br.response().read() 

#print html 

i = html.find("<a href=\"http")
j = html.find("\">",i)
url_new = html[i+9:j]

print url_new

#br.select_form(nr=0)
