/**
 * Created by dfitzgerald on 9/10/15.
 */

var addContactFromShareJbox = new jBox('Tooltip', {
    onOpen: function(){
        this.options.ajax.url = '/viewer/contact/new_contact_from_share/';
    },
    ajax: {
        reload: true
    },
    attach: $('#add_contact'),
    trigger: 'click',
    closeOnClick: 'body'
});