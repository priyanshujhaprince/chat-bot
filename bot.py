import google.generativeai as gpt

file=open("H:\\programing\\python programs\\gemini\\gemininew.txt","w")

prompt = input("hi in different languages")

gpt.configure(api_key='AIzaSyComl_nxG4UhsU6CNI2cniDjCAGCugUU6A')

geminipro = gpt.GenerativeModel('gemini-pro')


response = geminipro.generate_content(prompt)

print(response.text)

try:
    file.writelines(response.text)
    print("operation sucessfull")
except FileNotFoundError:
    print("error")

file.close()