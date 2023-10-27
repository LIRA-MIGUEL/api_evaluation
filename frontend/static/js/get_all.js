function getAll(){
    var request = new XMLHttpRequest;
    request.open('GET', "http://127.0.0.1:8000/contactos");
    request.send();

    request.onload = (e) => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("response" + json.response);

    };
};