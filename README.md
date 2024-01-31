<h1>Title:  Web Scrapping from Amazon Website using Python</h1>
<h2>Description: This project uses python to extract a single product detail from amazon website using libraries like requests, beautifulSoup.</h2>

<b>Installing Libraries</b>
<li>pip install requests</li>
<li>pip install beautifulsoup4</li>
 <p>  </p>
<b>STEPS:</b>

  
1. Import requests and beautifulsoup library.
   ( The 'requests' lib allows to send HTTP request of the web page and beautifulsoup lib allows to prase HTML conents)
2. Using 'user-agent' to send the request like a browser to the web server where the webpage is loaded.
   ( Websites like Amazon doesn't provide the HTML content easily, it will detect where the request comes from a browser or a compiler. So, we need to use 'user-agent' to send HTTP request like a browser does.
3. Once the HTML content is fetched, use Beautifulsoup to format the HTML. (Using soup.prettify())
4. Now, trace the HTML elements to find the content we search for. ( In this case, the title and the price of a product is traced using id and class elements where the content is stored)
5. The output is then stored to a file.
