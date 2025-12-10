/*!
=========================================================
* Steller Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// smooth scroll
$(document).ready(function(){
	$(".nav-link").on('click', function(event) {

    	if (this.hash !== "") {

			event.preventDefault();

			var hash = this.hash;

			$('html, body').animate({
				scrollTop: $(hash).offset().top
			}, 700, function(){
				window.location.hash = hash;
			});
      	} 
    });
});

// Dynamic Text Rotation for Contact Buttons
$(document).ready(function(){
    var translations = [
        { call: "Call Me", wa: "Whatsapp Me" },
        { call: "कॉल करें", wa: "व्हाट्सएप करें" },
        { call: "కాల్ చేయండి", wa: "వాట్సాప్ చేయండి" }
    ];

    var currentIndex = 0;

    setInterval(function() {
        currentIndex = (currentIndex + 1) % translations.length;
        var t = translations[currentIndex];

        $("#call-btn-text").text(t.call);
        $("#wa-btn-text").text(t.wa);
    }, 3000);
});