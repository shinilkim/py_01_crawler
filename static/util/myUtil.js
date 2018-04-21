var util = {
    tag : {
       clip: '<textarea id="clipboard_target" style="position:absolute;top:-9999em;"></textarea>'
    }
    ,clipboard: {
        copy: function(txt) {
            if( $("#clipboard_target").length == 0 ) {
                $("body").append(util.tag.clip);
            }
            $("#clipboard_target").val(txt).select();
            try{
                var successful = document.execCommand('copy');
                if(successful) {

                }
            } catch(e) {
                console.error('util.clipboard.copy() error: ',e);
            }
        }
    }
    // <button class="btn btn-xs btn-default hide _btn" id="btnJsonView" onclick="util.jsonView(this)" data-json="" data-target="response_body" data-status="text">json-viewer</button>
    ,jsonView: function(obj) {
            var obj = $(obj);
            var json = obj.data('json');
            var view = obj.data('status');
            var target = "#"+obj.data('target');
            try {
                var status = 'text';
                var name = '';
                if( view == 'text' ) {
                    status = 'json';
                    name = 'text-viewer';
                    var json2 = JSON.parse(json);
                    $(target).JSONView(json2, { collapsed: true, nl2br: true, recursive_collapser: true });
                    obj.removeClass("btn-default").addClass('btn-info');
                } else {
                    name = 'json-viewer';
                    $(target).text(json);
                    obj.removeClass("btn-info").addClass('btn-default');
                }

                obj.text(name);
                obj.data('status', status);
            } catch(e) {
                console.log('util.jsonView(this) error: ',e);
            }
    }

};
/* var today = new Date().format("yyyy-MM-dd");*/
Date.prototype.format = function(f) {
    if (!this.valueOf()) return " ";
    var weekName = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"];
    var d = this;
    return f.replace(/(yyyy|yy|MM|dd|E|hh|mm|ss|a\/p)/gi, function($1) {
        switch ($1) {
            case "yyyy": return d.getFullYear();
            case "yy": return (d.getFullYear() % 1000).zf(2);
            case "MM": return (d.getMonth() + 1).zf(2);
            case "dd": return d.getDate().zf(2);
            case "E": return weekName[d.getDay()];
            case "HH": return d.getHours().zf(2);
            case "hh": return ((h = d.getHours() % 12) ? h : 12).zf(2);
            case "mm": return d.getMinutes().zf(2);
            case "ss": return d.getSeconds().zf(2);
            case "a/p": return d.getHours() < 12 ? "오전" : "오후";
            default: return $1;
        }
    });
};

String.prototype.string = function(len){var s = '', i = 0; while (i++ < len) { s += this; } return s;};
String.prototype.zf = function(len){return "0".string(len - this.length) + this;};
String.prototype.replaceAll = function(org,dest) {return this.split(org).join(dest);}
String.prototype.trim = function() {return this.replace(/(^\s*)|(\s*$)/g, "");}
Number.prototype.zf = function(len){return this.toString().zf(len);};
Number.prototype.comma = function(){var regexp = /\B(?=(\d{3})+(?!\d))/g;return this.toString().replace(regexp, ',');}
