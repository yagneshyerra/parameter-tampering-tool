# parameter-tampering-tool
#Definition of parameter tampering

1.Parameter tampering refers to the unauthorized modification of input parameters in HTTP requests to manipulate the behavior of a web application. This form of attack occurs when an attacker modifies input parameters such as URL parameters, form fields, cookies, or HTTP headers to exploit vulnerabilities or bypass security controls implemented by the application.

2.clone the repository "https://github.com/yagneshyerra/parameter-tampering-tool.git"

3.run the python file CA3.py

4.by using command -->python3 CA3.py -m GET -u http://example.com -H "User-Agent: MyCustomAgent" -p "id=1" -p "name=test"

  a)we have to specify the HTTP method (GET, POST, PUT, DELETE) and target URL.
  
  b)Supports custom request headers (-H option) and URL parameters (-p option).
  
  c)Sends the HTTP request to the target URL using the specified method and parameters.

5.take a url to test if it is vulnerable to parameter tampering attack for eg:www.google.com
![git screen](https://github.com/yagneshyerra/parameter-tampering-tool/assets/122748437/4735eb46-6742-4f29-8988-3b5f6f8c8d20)

6.If the script is run with valid parameters and the HTTP request is successful, the output will display the response status code, headers, and body.
![image](https://github.com/yagneshyerra/parameter-tampering-tool/assets/122748437/fa59810b-b10b-4a0d-b6ff-b6cbd443c3f8)

7.if the given URL is vulnerable to parameter tampering attack we can by using this tool as shown in the image that "input validation bypass is detected!"
![image](https://github.com/yagneshyerra/parameter-tampering-tool/assets/122748437/9646dac1-5234-4441-9967-98d8bb8f572e)

this how this is used to detect that which URL is vulnerable to the parameter tampering attack.

8.if the given URL is not vulnerable to parameter tampering attack it wouldn't proceed any further or it will show error occurred (e.g., 404 Not Found) or it won't show any response status code. Let us take for example:www.techvertos.com.
![image](https://github.com/yagneshyerra/parameter-tampering-tool/assets/122748437/8ec68c77-590d-45cf-a9bd-1275dbf002c2)
