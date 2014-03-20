(function () {
    var rulesEle = document.getElementById('rules');
    var baseEle = document.getElementById('base');
    var submitEle = document.getElementById('submit');
    var resultsEle = document.getElementById('results');

    submitEle.addEventListener('click', function (evt) {
        var rules = cfg.parse(rulesEle.value);

        resultsEle.innerHTML = '';
        for (var i = 0; i < 10; i++) {
            resultsEle.innerHTML +=
                '<li><p>' + cfg.expand(baseEle.value, rules, []) + '</p></li>';
        }

        evt.preventDefault();
    });
})();
