https://github.com/zmap/ztag をpython3にポーティングしてzgrab2に対応

起動方法

`python3 senda-tool.py <ファイル名＞`

入力
- 　zgrab2の出力ファイル
- 　ファイル名のルール：　タイトル_port番号_プロトコル.json

 ___ 
## SSHの結果

```
/ __)/ __)( )_( )  ( )/ )( ___)( \/ )
\__ \\__ \ ) _ (    )  (  )__)  \  / 
(___/(___/(_) (_)  (_)\_)(____) (__) 

ѕєяνєя нσѕт кєу
fingerprint_sha256 : 5f3b470ac1c0f64f372357f4f5c7240cf04fa753573cacc72df8ea8a082fb721
rsa_public_key : {'exponent': 65537, 'modulus': 'oGth3Rb/v8TMRFOP7FpGGDN7JYk+cEvFsOjSATCNDYFW0jfah+d2imwUwGUALFF6hRjnnrAmN+SBqBhkgD3P7mw4J3wAkDezkAMnOpQXxGNs7oEZ3NiV3Qf/Aq/8As+gbjIpPJFLWD6fvnc+zTOGGaUcas4Lv+rPxdNUArry4aI7u6QZ6K4a17bl8m77BV1V7GvW88MnR+ICttEpU6x5fyxbBS7pcHqKz1CqyKu2dkIP1M+rXtgLNA0blUIymemJplfQj6/pdblG2F6uO7i1q8Vw5k05Gfb/7+YKWdLKVkCsis9ff4UlU9GGyHdPHeczB2AnbF5qAaLlnPcTlPjSrQ==', 'length': 2048}
key_algorithm : ssh-rsa
 ____    __    _  _  _  _  ____  ____ 
(  _ \  /__\  ( \( )( \( )( ___)(  _ \
 ) _ < /(__)\  )  (  )  (  )__)  )   /
(____/(__)(__)(_)\_)(_)\_)(____)(_)\_)

raw : SSH-2.0-OpenSSH_12.1
version : 2.0
software : OpenSSH_12.1
```
 ___ 
## TELNETの結果

```
 ____    __    _  _  _  _  ____  ____ 
(  _ \  /__\  ( \( )( \( )( ___)(  _ \
 ) _ < /(__)\  )  (  )  (  )__)  )   /
(____/(__)(__)(_)\_)(_)\_)(____)(_)\_)

NSD-105 release
Kernel 3.2.29 on an x86_64 (/dev/pts/0)
DS-20107ad6a484 login:
```

 ___ 
## HTTPSの結果

```
 ___  ___  __      _  _  ____  _  _ 
/ __)/ __)(  )    ( )/ )( ___)( \/ )
\__ \\__ \ )(__    )  (  )__)  \  / 
(___/(___/(____)  (_)\_)(____) (__) 

ιѕѕυєя
C=US, ST=CA, L=Santa Clara, O=Palo Alto Networks, OU=Support, CN=localhost, emailAddress=support@paloaltonetworks.com
ѕυвנєcт
C=US, ST=CA, L=Santa Clara, O=Palo Alto Networks, CN=a9258770d7e933091ab59d3c0b33870b5c7eed9d1256a140e1c47a67ff56439b, emailAddress=support@paloaltonetworks.com
ναℓι∂ιту
start : 2023-09-28T05:31:48Z
end : 2033-09-25T05:31:48Z
length : 315360000
ѕιgηαтυяє
valid : True
signature_algorithm : rsa
hash_algorithm : sha256
 _   _  ____  ____  ____    _   _  ____    __    ____   ____  ____ 
( )_( )(_  _)(_  _)(  _ \  ( )_( )( ___)  /__\  (  _ \ ( ___)(  _ \
 ) _ (   )(    )(   )___/   ) _ (  )__)  /(__)\  )(_) ) )__)  )   /
(_) (_) (__)  (__) (__)    (_) (_)(____)(__)(__)(____/ (____)(_)\_)

нєα∂єяѕ
allow : GET, HEAD, POST, PUT, DELETE, OPTIONS
cache_control : no-store, no-cache, must-revalidate, post-check=0, pre-check=0
connection : keep-alive
content_security_policy : default-src 'self'; script-src 'self' 'unsafe-eval' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;
content_type : text/html
etag : "ac85df00817"
expires : Thu, 19 Nov 1981 08:52:00 GMT
pragma : no-cache
strict_transport_security : max-age=31536000
x_content_type_options : nosniff
x_frame_options : SAMEORIGIN
x_xss_protection : 1; mode=block
 _   _  ____  ____  ____    ____  _____  ____   _  _ 
( )_( )(_  _)(_  _)(  _ \  (  _ \(  _  )(  _ \ ( \/ )
 ) _ (   )(    )(   )___/   ) _ < )(_)(  )(_) ) \  / 
(_) (_) (__)  (__) (__)    (____/(_____)(____/  (__) 

вσ∂у
<!DOCTYPE html>
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<base href="/">
<!--[if IE]>
    <script type="text/javascript">
        (function() {
            var baseTag = document.getElementsByTagName('base')[0];
            if (!(/^http/i).test(baseTag.href)) { // in case browser already translate to absolute path
                baseTag.href = location.protocol + '//' +  location.host +  baseTag.href;
            }
            baseTag.href = baseTag.href; // IE9 not correctly loading resources issue.
        })();
    </script>
<![endif]-->
<TITLE>Login</TITLE>
<!-- FIXME: need to use Page::includeStaticResource -->
<link rel="shortcut icon" type="image/x-icon" href="/login/images/favicon.ico">
<link rel="stylesheet" href="login/css/bootstrap.min.css">

<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<link rel="stylesheet" href="login/css/ie10-viewport-bug-workaround.css">
<link rel="stylesheet" href="login/css/login-admin.css">

<!--[if lt IE 9]>
<script src="login/js/html5shiv.min.js"></script>
<script src="login/js/respond.min.js"></script>
<![endif]-->

<script src="login/js/jquery.min.js"></script>
<script src="login/js/bootstrap.min.js"></script>

<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="login/js/ie10-viewport-bug-workaround.js"></script>

</HEAD>
  <body>
    <div class="loginscreen_logo">
      <img src="/login/images/logo-pan-48525a.svg" alt="">
      <div id="formdiv">
        <!-- BEGIN PAN_FORM_CONTENT -->
<!--suppress HtmlUnknownAttribute -->
<form name="login" id="login_form" method="post" action="" autocomplete="off">
<!-- hidden variables, we are going to set this to the session, bug fix 2157 -->
<input type="hidden" name="prot" value="">
<input type="hidden" name="server" value="">

<input type="hidden" name="authType" value="init">
<input type="hidden" name="challengeCookie" value="">

<div id="taLogin" >
<script src='js/3rdParty/es5-shim-3.4.0x/es5-shim.js'></script>
<script src='js/3rdParty/es5-shim-3.4.0/es5-sham.js'></script>
<script src='js/lib/lodash.js'></script>
<script src='js/lib/pan-extjs3.js'></script>
<script src='js/lib/global-store.js'></script>
<script src='js/lib/type-plus.js'></script>
<script src='js/lib/pan-json.js'></script>
<script src='js/lib/pan-logging.js'></script>
<script src='js/lib/pan-xml.js'></script>
<script src='js/lib/login.js'></script>
<script src='js/3rdParty/umd-0.4.10/umd.js'></script>
<script src='js/pan/_umd.require.config.js'></script>
<script src='js/pan/ext/util.js'></script>
<script src='js/pan/base/util.js'></script>
<script src='js/pan/base/msg.js'></script>
<script src='js/pan/base.js'></script>
<script src='js/pan/base/cookie.js'></script>
<script src='js/pan/test/QaAutomation.js'></script>
<script type="text/javascript">
var cacUserName = "";
// initialize upon load to let all browsers establish content objects
function initDHTMLAPI() {
    if (document.images) {
        window.isIE6CSS = (document.compatMode && document.compatMode.indexOf("CSS1") >= 0) ? true : false;
    }
    if(Ext.isIE){
        if (new RegExp(/msie ([0-9]{1,})/i).exec(navigator.userAgent) != null) {
            var rv = parseFloat( RegExp.$1 ); // ie version
            if (rv > 9) {
                // 10 and above
                Pan.base.cookie.set('isAboveIE10',rv);
            }
        }
    } else if (new RegExp(/trident/i).exec(navigator.userAgent) != null) {
        Pan.base.cookie.set('isAboveIE10','10'); // 11 and above always treat it as 10. Ext.isIE failed here
    }
}

// Return the available content width space in browser window

function getInsideWindowWidth() {
    if (window.innerWidth) {
        return window.innerWidth;
    } else if (isIE6CSS) {
        // measure the html elements clientWidth
        return document.body.parentElement.clientWidth;
    } else if (document.body && document.body.clientWidth) {
        return document.body.clientWidth;
    }
    return 0;
}

// Return the available content height space in browser window
function getInsideWindowHeight() {
    if (window.innerHeight) {
        return window.innerHeight;
    } else if (isIE6CSS) {
        // measure the html elements clientHeight
        return document.body.parentElement.clientHeight;
    } else if (document.body && document.body.clientHeight) {
        return document.body.clientHeight;
    }
    return 0;
}

function hideElement() {
    for (var i=0; i < arguments.length; i++) {
        var dv  = document.getElementById(arguments[i]);
        if(dv) {
            dv.style.display = "none";
        }
    }
}

function showWait(show){
    if(show){
        hideElement("trInitName", "trInitPwd", "trLoginBtn", 'trInitLocale');
        var dv = document.getElementById("wdiv");
        if(dv) dv.style.display="block";
    }
}

function get_url_param( name )
{
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( window.location.href );
    if( results == null )
        return "";
    else
        return results[1];
}

//
function loadPage() {

    initDHTMLAPI();

    var errMsg = "";
    if (0) {
        var issuesMsg = "<li>&lt;pre&gt;&lt;/pre&gt;";
        errMsg = issuesMsg;
    } else if (0) {
        var upgradeLogMsg = "<li>";
        errMsg = upgradeLogMsg;
    }

    var thisForm = document.getElementById("login_form");

    var respStatus = "Success";
    var redirectUrl = "";
    var showSaml = false;
    if (!showSaml) {
        hideElement('trSSO');
    }
    if (respStatus == "Warning") {
        var msg = "";
        alert(msg.replace(/&#039;/g, "'"));
        showWait(true);
        Pan.base.cookie.set("isFromLogin", "true", 1);
        window.location.href = redirectUrl;
    } else if (respStatus == "Error") {
        if (errMsg != "")
            errMsg += "<br><br>";

        errMsg += "<li>";
    } else if (respStatus == "Success") {
        if ("yes" == "yes") {
            if ("yes" == "no") {
                // no password needed
                if (!cacUserName) {
                    // if password is not needed and there is no user name it means cac check failed or something
                    errMsg += "<li>Insufficient credentials.";

                    // don't show any username/password fields and login button
                    hideElement("trInitName", "trInitPwd", "trLoginBtn", 'trInitLocale');
                } else {
                    thisForm.user.value = cacUserName;


                    // fill the authType field with "cacOnly" so that when we submit the form we know what to do
                    // at the back end
                    thisForm.authType.value = "cacOnly";

                    /* KK Test - for now it looks like this automatic submit is not working. Show
                     * the submit button for now. When we uncomment this we should move it to after
                     * showing/hiding the buttons below
                     // fill in stuff as if submit was clicked
                     submitClicked();

                     // then submit the form
                     thisForm.submit();
                     //document.getElementById("trLoginBtn").onclick();
                     */

                    // hide some of the fields in the form
                    hideElement("trInitName", "trInitPwd");
                    // showing the login button for now
                    //document.getElementById("trLoginBtn").style.display = "none";
                    document.getElementById("trLoginBtn").style.display = "block";

                    // show the creating user session message
                    document.getElementById("wdiv").style.display = "block";
                    document.getElementById("wdiv").innerHTML = "Click the login button to login as" + ' ' + cacUserName;
                }

            } else {
                // password needed, just go on to show the page

                // fill the userName field
                thisForm.user.value = cacUserName;
            }
        } else {
            // everything ok, just redirect to next page
            var expMsg = "";
            if (expMsg != "" ) {
                alert(expMsg);
                //document.getElementById("wdiv").innerHTML = "<span style=\"color:#166D7D\">" + expMsg + "</span><br>" + document.getElementById("wdiv").innerHTML ;
            }
            showWait(true);
            Pan.base.cookie.set("isFromLogin", "true", 1);
            window.location.href = redirectUrl;
        }
    } else if (respStatus == "Challenge") {
        // hide the init name/pwd row and show the challenge msg/pwd row
        hideElement("trInitName", "trInitPwd");
        document.getElementById("trChallengeMsg").style.display = "";
        document.getElementById("trChallengePwd").style.display = "";

        // fill the challenge msg field
        document.getElementById('spChallengeMsg').innerHTML = "";

        // fill the authType and challengeCookie field
        thisForm.authType.value = "challenge";
        thisForm.challengeCookie.value = "";

        // also fill the user field with the previously entered user name
        thisForm.user.value = user;

    }
    // respStatus can also be "" when we come to this page the first time

    if (errMsg != "") {
        var divObj = document.getElementById("dError");

        divObj.style.display = "block";
        divObj.innerHTML = errMsg;
    }

    if (document.login.user.value == '') {
        var nameRow = document.getElementById('trInitName');
        if (nameRow && nameRow.style.display != "none") {
            // use this to check if this field is visible
            document.login.user.focus();
        }
    }
}

function submitClicked() {
    var thisForm = document.getElementById("login_form");
    // hide the error div, just incase it was showing.
    var divObj = document.getElementById("dError");

    divObj.style.display = "none";
    divObj.innerHTML = "";

    // fill the hidden fields for prot and server, bug fix 2157
    var prot = window.location.protocol;
    var server = window.location.host;
    //alert("prot: " + prot + ", server: " + server);
    thisForm.prot.value = prot;
    thisForm.server.value = server;
}

function submitSamlClicked() {
    var thisForm = document.getElementById("login_saml_form");
    thisForm.submit();
    return true;
}

function checkCapsLock(e){
    var el = document.getElementById('divcl');
    if (!el) return;

    var keycode = e.keyCode? e.keyCode : e.which;
    var shift = e.shiftKey? e.shiftKey : !!(keycode == 16);

    if((keycode >= 65 && keycode <= 90 && !shift) || (keycode >= 97 && keycode <= 122 && shift))
        el.style.visibility = 'visible';
    else
        el.style.visibility = 'hidden';
}

function checkCapsLockChallenge(e){
    var el = document.getElementById('divclChallenge');
    if (!el) return;

    var keycode = e.keyCode? e.keyCode : e.which;
    var shift = e.shiftKey? e.shiftKey : !!(keycode == 16);

    if((keycode >= 65 && keycode <= 90 && !shift) || (keycode >= 97 && keycode <= 122 && shift))
        el.style.visibility = 'visible';
    else
        el.style.visibility = 'hidden';
}

function checkSubmitBtnAvail() {
    var user = Ext.get('user');
    var passwd = Ext.get('passwd');
    var challengePwd = Ext.get('challengePwd');
    var loginBanner = Ext.getCmp('bannerFieldSet');

    var avail = true;
    var submitBtn = Ext.get('submit');

    if (Ext.fly('trInitName').dom.style.display !== 'none') {
        avail = avail && !!user.getValue();
    }

    if (Ext.fly('trInitPwd').dom.style.display !== 'none') {
        avail = avail && !!passwd.getValue();
    }

    if (Ext.fly('trChallengePwd').dom.style.display !== 'none') {
        avail = avail && !!challengePwd.getValue();
    }

    if (loginBanner && loginBanner.getValue) {
        avail = avail && loginBanner.getValue();
    }

    submitBtn.dom.disabled = !avail;
}

Ext.onReady(function(){
    var ml = 20;
    ml = 63;
    var btn = Ext.get('submit');
    if (btn) {
        btn.on('click', submitClicked);
    }
    var user = Ext.get('user');
    if (user && user.dom) {
        var u = Ext.get('user').dom;
        var uname = Pan.base.param('user') || '';
        if (uname) {
            u.value = uname;
        }
        u.maxlength = ml;
    }
    loadPage();

    var loginForm = Ext.get('login_form');
    var passwd = Ext.get('passwd');
    var checkSubmitBtnAvailHandler = function() {
        checkSubmitBtnAvail();
    };
    loginForm.on('click', checkSubmitBtnAvailHandler);
    loginForm.on('keyup', checkSubmitBtnAvailHandler);
    user.on('change', checkSubmitBtnAvailHandler);
    passwd.on('change', checkSubmitBtnAvailHandler);

    var msgE = Ext.getDoc().child('.msg');
    if (msgE) {
        if (Ext.isIE8) {
            var prefMaxWidth = msgE.getStyle('max-width').replace(/px$/, '');
            var prefMaxHeight = msgE.getStyle('max-height').replace(/px$/, '');
            if (msgE.getHeight() > prefMaxHeight) {
                msgE.setHeight(prefMaxHeight);
            }
            if (msgE.getWidth() > prefMaxWidth) {
                msgE.setWidth(prefMaxWidth);
            }
        }
        if ("") {
            var fieldSet = Ext.create({
                id: "bannerFieldSet",
                title: "I Accept and Acknowledge the Statement Below",
                xtype: "fieldset",
                checkboxToggle: true,
                width: 550,
                autoScroll: true,
                onCheckClick: function() {
                    checkSubmitBtnAvail();
                },
                getValue: function() {
                    if (this.checkbox) {
                        return this.checkbox.dom.checked;
                    }
                },
                renderTo: 'motd',
                bodyCfg: {
                    html: msgE.dom.innerHTML
                }

            });
            fieldSet.checkbox.dom.checked = false;
        } else {
            Ext.fly('motd').appendChild(msgE);
            msgE.setStyle({visibility: 'visible'});
        }
    }

    checkSubmitBtnAvail();
});

if( self == top ) {
    document.documentElement.style.display = 'block' ;
} else {
    top.location = self.location ;
}

function doSubmit(thisform)
{
    return true;
}
</script>
    <div id="wdiv" style="display: none;">
        Creating administrative session. Please wait...    </div>
    <div id="dError" style="display: none;">
        Invalid username or password
    </div>
    <table>
        <tr id="trInitName" style="display: table-row;">
            <td>
                <label for="user">
                    Username                </label>
            </td>
            <td><input type="text" id="user" name="user" size="19"></td>
        </tr>
        <tr id="trInitPwd" style="display: table-row;">
            <td>
                <label for="passwd">
                    Password                </label>
            </td>
            <td>
                <input type="password" style="display:none"> <!-- Work around to disable password autofill from browser -->
                <input type="password" maxlength="63" size="19" id="passwd" name="passwd" onkeypress="checkCapsLock(event);">
                <span id="divcl" style="visibility: hidden;"><img src="images/ssl_decryption.gif" title="CAPS LOCK" alt="CAPS LOCK" /></span>
            <td>
        </tr>
        <tr id="trInitLocale" style="display: none;">
            <td>Language</td>
            <td></td>
            <td></td>
        </tr>
        <tr id="trChallengeMsg" style="display: none;">
            <td></td>
            <td id="spChallengeMsg">Enter Management UI's PASSCODE</td>
        </tr>
        <tr id="trChallengePwd" style="display: none;">
            <td>
                <label for="challengePwd"></label>
            </td>
            <td>
                <input type="password" name="challengePwd" id="challengePwd" size="19" maxlength="63" onkeypress="checkCapsLockChallenge(event);">
                <span id="divclChallenge" style="visibility: hidden;"><img src="images/ssl_decryption.gif" title="CAPS LOCK" alt="CAPS LOCK" /></span>
            </td>
        </tr>
        <tr id="trLoginBtn" style="display: table-row;">
            <td></td>
            <td>
                <input class="buttonFixed" type="submit" id="submit" name="ok" value="Log In" onclick="return doSubmit(this.form);">
                  <span id="trSSO" class="login_option" style="display: inline-block;">
                    <a href="javascript:void(0)" onclick="return submitSamlClicked();">Use Single Sign-On</a>
                  </span>
            </td>
        </tr>
    </table>
    <div id="motd">
    </div>
</div>
</form>
<!-- END PAN_FORM_CONTENT -->
<!-- FORM for SAML -->
<form name="login_saml" id="login_saml_form" method="post" action="">
    <input name="loadSamlForm" value="true" type="hidden"/>
</form>
      </div>
    </div>
    <div class="msg" style="visibility: hidden;">
            </div>
  </body>
</HTML>

<!--
         __LOGIN_PAGE__
-->

<!--
         __LOGIN_PAGE_FOR_PANORAMA_BACKWARD_COMPATIBILITY__
-->


ƬIƬLƐ
Login
ƇOƤƳRIƓHƬ

SƇRIƤƬ SƇR
login/js/jquery.min.js
login/js/bootstrap.min.js
login/js/ie10-viewport-bug-workaround.js
js/3rdParty/es5-shim-3.4.0x/es5-shim.js
js/3rdParty/es5-shim-3.4.0/es5-sham.js
js/lib/lodash.js
js/lib/pan-extjs3.js
js/lib/global-store.js
js/lib/type-plus.js
js/lib/pan-json.js
js/lib/pan-logging.js
js/lib/pan-xml.js
js/lib/login.js
js/3rdParty/umd-0.4.10/umd.js
js/pan/_umd.require.config.js
js/pan/ext/util.js
js/pan/base/util.js
js/pan/base/msg.js
js/pan/base.js
js/pan/base/cookie.js
js/pan/test/QaAutomation.js
```

