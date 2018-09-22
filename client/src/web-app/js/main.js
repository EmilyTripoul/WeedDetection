/******************************************
 *  Author : Emily
 *  Created On : Sat Sep 15 2018
 *  File : main.js
 *******************************************/

function py_dummy(arg) {}

function py_wrapPromise(pyFunc, ...args) {
    return new Promise(function(resolve, reject) {
        pyFunc(...args, function(data) {
            resolve(data)
        })
    })
}

$(function() {
  $("#top-menu-content").menu();
  $("value").val();
  $("button").button();

  (function() {
    let uiIconLoad = "icon-loader";
    let uiIconValid = "icon-valid";
    let uiIconError = "icon-error";

    let loginErrorMsg = $("#login-error-message");
    let loginButton = $("#login-button-confirm");
    let loginImg = $("#login-validation-img");
    let loginModal = $("#login-modal");

    function loginStyleReset() {
      loginErrorMsg.hide();
      loginImg.removeClass(uiIconLoad);
      //loginButton.button("enable");
    }

    function onLoginButtonConfirm() {
        debugLog('Login : Connection success');
      loginStyleReset();
      loginImg.addClass(uiIconValid);
      loginModal.slideUp("slow");
    }
    function onLoginButtonReject() {
      debugLog('Login : Connection failed');
      loginStyleReset();
      loginErrorMsg.show();
      loginImg.addClass(uiIconError);
    }

    $("#login-button-confirm").click(function(event) {
        loginImg.addClass(uiIconLoad);
        loginImg.removeClass(uiIconValid);
        loginImg.removeClass(uiIconError);
  
        //loginButton.button("disable");

      let loginEmail = $("#login-input-email").val();
      let loginPassword = $("#login-input-password").val();
      let loginServer = $("#login-input-server").val();


      let data = {
        loginEmail: loginEmail,
        loginPassword: loginPassword,
        loginServer: loginServer
      };

      debugLog('Login : Connection attempt...');

      let promiseLogin = new Promise(function(resolve, reject) {
        py_wrapPromise(py_validateLogin, data).then(function (value) {
            let validateLoginResults = value;
            if (validateLoginResults == 1 ) {
              resolve();
            } else {
              reject();
            }
        });
      });

      promiseLogin.then(onLoginButtonConfirm, onLoginButtonReject);
    });

    py_getLoginInfo(function (data) {
        data=data || {};
        
        let loginEmail = data['email'];
        let loginPassword = data['password'];
        let loginServer = data['server'] || 'my.farm.bot';
        
        if (loginEmail!=undefined) {
            debugLog('Login : Loading login info from file');
            $("#login-input-email").val(loginEmail);
            $("#login-input-password").val(loginPassword);
        }
        $("#login-input-server").val(loginServer);
    })


  })();
});

function getTimeString() {
    var currentdate = new Date(); 
    return "[" + currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/" 
                + currentdate.getFullYear() + " @ "  
                + currentdate.getHours() + ":"  
                + currentdate.getMinutes() + ":" 
                + currentdate.getSeconds() + "] ";
};

function debugLog(message) {
    let consoleArea=$("#debug-textarea")[0];
    if (typeof message == 'object') {
        consoleArea.innerHTML= consoleArea.innerHTML + getTimeString() + JSON.stringify(message)+'\n';
    } else {
        consoleArea.innerHTML= consoleArea.innerHTML + getTimeString() + message+'\n';
    }
    consoleArea.scrollTop = consoleArea.scrollHeight;
};

/*
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
    };*/
