/******************************************
 *  Author : Emily   
 *  Created On : Sat Sep 15 2018
 *  File : main.js
 *******************************************/

$(function(){
    $( "#top-menu-content" ).menu();

})

    function js_print(lang, event, msg) {
        msg = "<b class="+lang+">"+lang+": "+event+":</b> " + msg;
        console = document.getElementById("console")
        console.innerHTML += "<div class=msg>"+msg+"</div>";
    }
    function js_callback_1(ret) {
        js_print("Javascript", "html_to_data_uri", ret);
    }
    function js_callback_2(msg, py_callback) {
        js_print("Javascript", "js_callback", msg);
        py_callback("String sent from Javascript");
    }
    window.onload = function(){
        js_print("Javascript", "window.onload", "Called");
        js_print("Javascript", "python_property", python_property);
        js_print("Javascript", "navigator.userAgent", navigator.userAgent);
        js_print("Javascript", "cefpython_version", cefpython_version.version);
        html_to_data_uri("test", js_callback_1);
        external.test_multiple_callbacks(js_callback_2);
    };
     	