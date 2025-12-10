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
    var $callText = $("#call-btn-text");
    var $waText = $("#wa-btn-text");

    // Add transition class initially
    $callText.addClass("text-transition");
    $waText.addClass("text-transition");

    setInterval(function() {
        // Fade out
        $callText.addClass("text-hidden");
        $waText.addClass("text-hidden");

        // Wait for fade out to complete (500ms matches CSS)
        setTimeout(function() {
            currentIndex = (currentIndex + 1) % translations.length;
            var t = translations[currentIndex];

            $callText.text(t.call);
            $waText.text(t.wa);

            // Fade in
            $callText.removeClass("text-hidden");
            $waText.removeClass("text-hidden");
        }, 500);

    }, 3000);
});