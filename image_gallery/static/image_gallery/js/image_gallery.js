if (jQuery == undefined && django.jQuery != undefined){
	var jQuery = django.jQuery;
}

var gallery_upload_url;
function initGallery(url){
	gallery_upload_url = url
}

function GalleryImageDelete(id, img_id){
	elem = jQuery('#'+id+'-img'+img_id).parents('.gallery-image')
	elem.fadeOut("slow", function() {
		del = jQuery(".button-delete")
		list = jQuery('#'+id+'-thumbnails')
		del.appendTo(list)
		del.hide()
		jQuery(this).remove()
		jQuery('#'+id).val('')
		jQuery('#'+id+'-thumbnails').find('img[id^='+id+'-img]').each(function(index){
			var img_id = jQuery(this).attr('id')
			img_id = img_id.slice((id+'-img').length)
			addValue(id, img_id)
		})
		showFileButton(id);
	})
/*
	$.ajax({
		type: "POST",
		url: window.gallery_delete_url,
		data: { id: img_id },
		complete: function (data)
		{
			var response = jQuery.parseJSON(data.responseText)
			if (response.success){

			}
		}
	});
*/
}

function GalleryImageChange(id){
	loading = jQuery('#'+id+'-loading')
	list = jQuery('#'+id+'-thumbnails')
	var form_id = new Date().getTime()
	form = createUploadForm(form_id, id + '-file')
	form.ajaxSubmit({
		url: gallery_upload_url,
	    beforeSend: function() {
	    	loading.appendTo(list)
	    	loading.show()
	    },
		complete: function (data)
		{
			loading.hide()
			var response = jQuery.parseJSON(data.responseText)
			if (response.success){
				jQuery('#'+id+'-errors-block').hide()
		        html = '<div class="gallery-image" onclick="GalleryImageDelete(\''+id+'\', \''+response.id+'\')" onmouseover="showButton(\''+id+'\', \''+response.id+'\')" onmouseout="hideButton(\''+id+'\', \''+response.id+'\')">'
		        html += '<div><img id="'+id+'-img'+response.id+'" src="'+response.url+'"></div>'
        		var img = jQuery(html)
				img.appendTo(list)

				addValue(id, response.id)
			}
			else{
				jQuery('#'+id+'-errors-block').show()
				jQuery('#'+id+'-errors-text').html(response.message)
			}
			showFileButton(id);
		}
	});
}


function createUploadForm(id, fileElementId)
{
	//create form
	var formId = 'jUploadForm' + id;
	var fileId = 'jUploadFile' + id;
	var form = jQuery('<form  action="" method="POST" name="' + formId + '" id="' + formId + '" enctype="multipart/form-data"></form>');

	// csrf
	var csrf_value = jQuery('#' + fileElementId).parents('form').find('[name=csrfmiddlewaretoken]').val();
	var csrf = '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrf_value + '">';
	jQuery(csrf).appendTo(form);

	var oldElement = jQuery('#' + fileElementId);
	var newElement = jQuery(oldElement).clone();
	jQuery(oldElement).attr('id', fileId);
	jQuery(oldElement).before(newElement);
	jQuery(oldElement).appendTo(form);


	//set attributes
	jQuery(form).css('position', 'absolute');
	jQuery(form).css('top', '-1200px');
	jQuery(form).css('left', '-1200px');
	jQuery(form).appendTo('body');
	return form;
}

function addValue(id, value)
{
	elem = jQuery('#'+id)
	if (elem.val()){
		new_val = elem.val() + ',' + value
	}
	else{
		new_val = value
	}
	elem.val(new_val)
}

function showButton(id, img_id){
	del = jQuery(".button-delete")
	img = jQuery('#'+id+'-img'+img_id)
	del.appendTo(img.parent())
	del.show()
	img.parent().css('background', '#000000')
	img.css("opacity", "0.5")

}
function hideButton(id, img_id){
	del = jQuery(".button-delete")
	img = jQuery('#'+id+'-img'+img_id)
	del.appendTo(img.parent())
	del.hide()
	img.parent().css('background', 'none')
	img.css("opacity", "1")
}

function showFileButton(id){
	file_input = jQuery('#'+id+'-file')
	var max_images = file_input.attr('max_images')
	if (max_images != undefined){
		if (jQuery('#'+id+'-thumbnails .gallery-image').length - 1 >= max_images){
			file_input.hide();
		}else{
			file_input.show();
		}
	}
}
