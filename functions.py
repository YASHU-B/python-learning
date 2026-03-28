def greet(name):
    return f"Hello {name}!"

print(greet("yashu"))    

# defalut parameters 
def wel(name, lang="english"):
    if lang == "telugu":
        return f"Namaste,{name}!"
    return f"Hello, {name}!"

print(wel("yashu", "telugu"))
print(wel("bunny"))
