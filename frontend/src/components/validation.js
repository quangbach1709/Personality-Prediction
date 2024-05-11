$().ready(function() {
	$("#questionForm").validate({
		onfocusout: false,
		onkeyup: false,
		onclick: false,
		rules: {
			"gender": {
				required: true
			},
			"age": {
				required: true
			},
			"question": {
				require: true
			}
		},
        messages: {
			"gender": {
				required: "Hãy chọn giới tính",
			},
			"age": {
				required: "Hãy nhập tuổi"
			},
			"question": {
				equalTo: "Hãy chọn đáp án"
			}
		}
	});
});