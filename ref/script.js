//alert source: https://sweetalert.js.org
//scrollbar source: https://medium.com/spemer/customize-websites-scrollbar-with-css-270ca436d6c1
//download source: https://micropilot.tistory.com/2253
//platform filter source: https://stove99.tistory.com/87

$(document).ready(function () {
    var filter = "win16|win32|win64|mac|macintel";
    var userAgent = navigator.userAgent.toLowerCase();
    var isIE = userAgent.indexOf('trident');
    var chk = false;

    if (navigator.platform) {
        if (filter.indexOf(navigator.platform.toLowerCase()) < 0) {
            //페이지에 접속한 기기가 모바일일 경우 해당 콘텐츠를 활성화한다
            $('*').css('visibility', 'hidden');
            $('.mobile-content').css('visibility', 'visible');
            $('.small-screen-content').css('visibility', 'hidden');
        }
    }


    //모드 리스트 아이콘
    $('#mod-list').click(function () {
        if (chk == false) {
            $("summary > i").attr('class','fas fa-angle-up');
            chk = true;
        }else {
            $("summary > i").attr('class','fas fa-angle-down');
            chk = false;
        }
    });

    //다운로드
    $('#btnDownload').click(function (e) {
        var d = new Date();
        var date = d.getDay();
        if (true) { // date == 1 || date == 2
            swal({
                text: "다운로드 하시겠습니까?",
                buttons: ["아니요", "예"],
            })
                .then((willDelete) => {
                    if (willDelete) {
                        swal({
                            title: "다운로드 시작",
                            text: "약간의 시간이 소요되며,\n사용자가 몰릴 경우에 다운로드가 지연될 수 있습니다.",
                            icon: "success",
                            button: "확인"
                        });
                        $('#downloadLink').prop('href', 'https://bearyu.kr/download/rutae/루태100인_시참_Armourers_Workshop.zip');
                        $('#downloadLink').prop('download', '루태100인_시참_Armourers_Workshop.zip');
                        $('#downloadLink')[0].click();
                    }
                });
        }else {
            swal({
                title: "다운로드 불가",
                text: "시청자 참여 기간이 아닙니다.",
                button: "확인",
                dangerMode: true
            })
        }

    });
});

$(document).on('click', function (e) {
    if (e.target.id == 'download-content') {
        if ($("#btnDownload").is(':disabled')) {
            swal({
                title: "다운로드 불가",
                text: "주의사항 확인란에 체크하지 않아 다운로드할 수 없습니다",
                button: "확인",
                dangerMode: true
            })
        }
    }
});

function agree() {
    var chk = document.getElementById('chk');
    if ($(chk).prop("checked")) {
        $('button').prop('disabled', false);
        document.getElementById("btnDownload").style.pointerEvents = "all";
    } else {
        $('button').prop('disabled', true);
        document.getElementById("btnDownload").style.pointerEvents = "none";
    }
}