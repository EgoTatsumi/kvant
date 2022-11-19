function req_get_title(id){
    $.ajax({
        url: "get_title", //  url-адрес, по которому посылается запрос
        type: "GET", // http-метод передачи данных
        data: { link : document.getElementById("link").value,
                btn_id : id }, // данные, отправляемые c запросом на сервер
        dataType: "text", // тип даных, ожидаемых в ответе сервера
        // в случае успешного запроса
        success : function(result, status) {
            console.log("success");
            console.log(status);
            document.getElementById("title").value = result
            },
        // в случае неудачного запроса
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
            }
    });
};
