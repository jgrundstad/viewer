/**
 * Created by Dominic Fitzgerald on 10/7/15.
 */
$(document).ready(function(){
    $('select[name=study]').change(function(){
        var study_id = $(this).val();
        var options = [];
        var request_url = '/viewer/get_bnids_by_study/' + study_id + '/';
        $.getJSON(
            request_url,
            function(data){
                $.each(data, function(key, val) {
                    options.push('<option value="' + key + '">' + val + '</option>');
                });
                $('select[name=bnids]').html(options.join('\n'));
            }
        );
    });

    $('select[name=bnids]').empty();

    new jBox('Modal', {
        attach: $('.igsbviewer-modal-add-button'),
        ajax: {
            url: '/viewer/report/upload_report'
        },
        overlay: true,
        closeOnClick: 'overlay',
        closeButton: 'box'
    });
    var $modalEditButton = $('.igsbviewer-modal-edit-button');
    $modalEditButton.click(function(){
        pk = $(this).data('pk');
    });
    new jBox('Modal', {
        onOpen: function(){
            this.options.ajax.url = '/viewer/report/edit_report/' + pk;
        },
        ajax: {
            reload: true
        },
        attach: $modalEditButton,
        overlay: true,
        closeOnClick: 'overlay',
        closeButton: 'box'
    });

    /* Set up 'delete' modal box */
    var pk = 0;
    var $modalDeleteButton = $('.igsbviewer-modal-delete-button');

    $modalDeleteButton.click(function(){
        pk = $(this).data('pk');
    });
    new jBox('Modal', {
        onOpen: function(){
            this.options.ajax.url = '/viewer/report/delete_report/' + pk;
        },
        ajax: {
            reload: true
        },
        attach: $modalDeleteButton,
        overlay: true,
        closeOnClick: 'overlay',
        closeButton: 'box'
    });


    /* Share button */
    var $modalShareButton = $('.igsbviewer-modal-share-button');
    $modalShareButton.click(function(){
        pk = $(this).data('pk');
    });
    new jBox('Modal', {
        onOpen: function(){
            this.options.ajax.data = function(){
                var reportIds = [];
                $('.multiplereports').filter(':checked').each(function(){
                    reportIds.push('reportid=' + $(this).data('reportid'));
                });
                if(reportIds.length < 1){
                    $(this).close();
                    return false;
                }
                return reportIds.join('&');
            }();
        },
        ajax: {
            reload: true,
            url: '/viewer/shared/share_report/'
        },
        attach: $('#share-reports'),
        overlay: true,
        closeOnClick: 'overlay',
        closeButton: 'box'
    });

    $(".igsbviewer-view-report").click(function(){
        var pk = $(this).data('pk');
        var $csrf = $($(this).data('csrf'));
        console.log('clicked ' + pk);
        $("<form>").attr({
            action: '/viewer/report/view_report/' + pk + '/',
            method: 'POST'
        }).append($csrf).appendTo($("body")).submit();
    });

    $('#information-dashboard').click(function(){
        var reportIds = [];
        $('.multiplereports').filter(':checked').each(function(){
            reportIds.push($(this).data('reportid'));
        });
        if(reportIds.length < 1){
            return false;
            // Do something more informative? TODO
        }

        /* Extract report IDs and add to form, submit */
        var $form = $('<form>').attr({
            method: 'get',
            action: '/viewer/info/'
        });
        for(var i = 0; i < reportIds.length; i++){
            $('<input>').attr('name', 'reportIds[]').val(reportIds[i]).appendTo($form);
        }
        $form.submit();
    });

    $('#download-reports').click(function(){
        reportIds = [];
        $('.multiplereports').filter(':checked').each(function(){
            reportIds.push($(this).data('reportid'));
        });
        if(reportIds.length < 1){
            return false;
            // Do something more informative? TODO
        }
        console.log(reportIds);

        $.get('/viewer/report/zip-and-download/', {reportids: reportIds}, function(data){
            window.location.href = data;
        });
    });
});
