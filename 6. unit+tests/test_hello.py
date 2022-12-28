from hello import hello

def test_hello():
    assert hello() == "hello world"

def test_arguement():
    for name in ["herm", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"
    
    assert hello("David") == "hello, David"
# make test short and simple to reduce tests of tests   


