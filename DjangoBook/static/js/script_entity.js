// https://docs.djangoproject.com/en/3.1/ref/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var xhr;

function createEntity() {
    //event.preventDefault();

    var strurl = "entity_create";
    //alert(strurl);
    //return false;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            var data = xhr.responseText;

            var obj = JSON.parse(data);
            //alert(obj.result_msg);
            var node = document.createElement("TR");
            node.innerHTML = obj.txtString;
            document.getElementById("tbody").appendChild(node);
            location.reload();

        }
    };
    xhr.open("GET", strurl);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(null);

};

function createMeta(elem) {

    var eid = elem.getAttribute('eid');
    var ctype = elem.innerHTML;

    var strurl = "meta_create?eid=" + eid + "&ctype=" + ctype;
    //alert(strurl);
    //return false;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            var data = xhr.responseText;

            document.getElementById("etitle_"+eid).click();
        }
    };
    xhr.open("GET", strurl);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(null);

};

function readMeta(elem) {

    var eid = elem.getAttribute('eid');

    var strurl = "meta_read?eid=" + eid;
    //alert(strurl);
    //return false;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            var data = xhr.responseText;

            var obj = JSON.parse(data);
            document.getElementById("metabox_"+eid).style.display = "block";
            document.getElementById("metabox_"+eid).innerHTML = obj.metastring;
        }
    };
    xhr.open("GET", strurl);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(null);

};

function createTable(elem) {

    var eid = elem.getAttribute('eid');

    var strurl = "table_create?eid=" + eid;
    //alert(strurl);
    //return false;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            var data = xhr.responseText;

            var obj = JSON.parse(data);
            if(obj.error == 'Y') {
                alert(obj.result_msg);
            }
            else {
                location.reload();
            }
        }
    };
    xhr.open("GET", strurl);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(null);

};

function generateCode(elem) {

    var eid = elem.getAttribute('eid');
    var flag = elem.innerHTML;

    if(flag == 'Data') {
        var strurl = "codecreate_data?eid=" + eid;
    }
    else if(flag == 'View') {
        var strurl = "codecreate_view?eid=" + eid;
    }
    else if(flag == 'Temp') {
        var strurl = "codecreate_template?eid=" + eid;
    }
    else if(flag == 'Config') {
        var strurl = "codecreate_config?eid=" + eid;
    }
    else {
        return false;
    }

    //alert(strurl);
    //return false;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            var data = xhr.responseText;

            var obj = JSON.parse(data);
            alert(obj.result_msg);
            if(flag == 'Config') {
                location.reload();
            }
        }
    };
    xhr.open("GET", strurl);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(null);

};

