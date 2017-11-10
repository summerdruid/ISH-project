$(document).ready(function(){
	// maybe adapt this later to load xml?
	$("#uploader").click(function(){
		console.log("Uploader has been clicked.");
	});

	$('input[type="file"]').change(function(){
		var file = document.getElementById("uploader").files[0];
		var reader = new FileReader()
		reader.readAsText(file)
		parser = new DOMParser();
		reader.onloadend = function() {
			eqfeed_callback($(reader.result))
		}	

		$("#image-viewer").append("blah blah");
	});
});
