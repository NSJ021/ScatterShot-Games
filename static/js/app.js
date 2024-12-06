$(function () {
    "use strict";

    // Activate Magnify on portfolio items
    $(".portfolio-item").magnificPopup({
        delegate: "a",
        gallery: { enabled: true },
        type: "image"
    });

    // Activate LightGallery
    $(".game-magnify-gallery").lightGallery();

    // Call header and layout adjustment functions
    adjustHeader();
    doSticky();
    placedDashboard();

    // Window scroll and resize event listeners
    $(window).on("scroll", () => {
        adjustHeader();
        doSticky();
        placedDashboard();
    });

    $(window).on("resize", () => {
        adjustHeader();
        doSticky();
        placedDashboard();
    });

    function adjustHeader() {
        const windowWidth = $(window).width();
        if (windowWidth > 0) {
            if ($(document).scrollTop() >= 100) {
                if ($(".header-shrink").length === 0) {
                    $(".sticky-header").addClass("header-shrink");
                }
                if ($(".do-sticky").length === 0) {
                    $(".company-logo img").attr("src",
                        "static/img/logos/logo.jpg");
                }
            } else {
                $(".sticky-header").removeClass("header-shrink");
                if (
                    $(".do-sticky").length === 0 &&
                    $(".fixed-header").length === 0 &&
                    $(".fixed-header2").length === 0
                ) {
                    $(".company-logo img").attr("src",
                        "static/img/logos/logo.jpg");
                } else {
                    $(".company-logo img").attr("src",
                        "static/img/logos/logo.jpg");
                }
            }
        } else {
            $(".company-logo img").attr("src",
                "static/img/logos/logo.jpg");
        }
    }

    function doSticky() {
        if ($(document).scrollTop() > 40) {
            $(".do-sticky").addClass("sticky-header");
        } else {
            $(".do-sticky").removeClass("sticky-header");
        }
    }

    function placedDashboard() {
        const headerHeight = parseInt($(".main-header").height(), 10);
        $(".dashboard").css("top", headerHeight);
    }

    // Initialize page scroller
    $.scrollUp({
        animation: "fade",
        animationSpeed: 200,
        easingType: "linear",
        scrollDistance: 300,
        scrollFrom: "top",
        scrollImg: false,
        scrollName: "page_scroller",
        scrollSpeed: 500,
        scrollText: "<i class='fa fa-chevron-up'></i>",
        zIndex: 2147483647
    });

    // Initialize select picker
    $(".selectpicker").selectpicker();

    // Initialize partner carousel
    (() => {
        $("#ourPartners").carousel({ interval: 3600 });
    })();

    $(".our-partners .item").each((index, element) => {
        let itemToClone = $(element);
        for (var i = 1; i < 4; i++) {
            itemToClone = itemToClone.next();
            if (!itemToClone.length) {
                itemToClone = $(element).siblings(":first");
            }
            itemToClone
                .children(":first-child")
                .clone()
                .addClass(`cloneditem-${i}`)
                .appendTo($(element));
        }
    });

    // Initialize Slick sliders
    $(".slick-carousel").each(function () {
        const slider = $(this);
        slider.slick({
            infinite: true,
            dots: false,
            arrows: false,
            centerMode: true,
            centerPadding: "0",
        });
        slider
            .closest(".slick-slider-area")
            .find(".slick-prev")
            .on("click", () => {
                slider.slick("slickPrev");
            });
        slider
            .closest(".slick-slider-area")
            .find(".slick-next")
            .on("click", () => {
                slider.slick("slickNext");
            });
    });

    // Fade out messages after timeout
    setTimeout(() => {
        $("#message").fadeOut("slow");
    }, 4000);
});
