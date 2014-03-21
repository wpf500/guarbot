(function () {
    var subjectEle = document.getElementById('subject');
    var submitEle = document.getElementById('submit');
    var resultsEle = document.getElementById('results');
    var articleEle = document.getElementById('article');
    var expansionEle = document.getElementById('expansion');
    var rulesEle = document.getElementById('rules');

    var prevSubject, subjects = {};
    var baseRules;

    var rulesTemplate = [
        '<div class="row">',
            '<div class="col-sm-2 text-right"><b>{rule_name}</b></div>',
            '<div class="col-sm-10">{values}</div>',
        '</div>',
        '<hr />'
    ].join('');

    var valuesTemplate = '<p>{value}</p>';

    var expansionTemplate = [
        '<ul>',
            '<li>',
                '{rule_name} - {rule}',
                '{subtree}',
            '</li>',
        '</ul>'
    ].join('');

    function mergeRules(a, b) {
        var ret = JSON.parse(JSON.stringify(a));
        for (ruleName in b) {
            if (!ret[ruleName]) {
                ret[ruleName] = [];
            }
            ret[ruleName] = ret[ruleName].concat(b[ruleName]);
        }
        return ret;
    }

    function loadRules(subject, callback) {
        if (subjects[subject]) {
            callback(subjects[subject]);
        } else {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var rules = JSON.parse(xhr.responseText);
                    rules['SUBJECT'] = [subject];
                    subjects[subject] = rules;
                    callback(rules);
                }
            };

            xhr.open('GET', 'static/data/' + subject + '.json', true);
            xhr.send();
        }
    }

    function printExpansion(tree) {
        return tree.map(function (subtree) {
            var html = expansionTemplate
                .replace('{rule_name}', subtree[0])
                .replace('{rule}', subtree[1])
                .replace('{subtree}', printExpansion(subtree[2]));
            return html;
        }).join('');
    }

    submitEle.addEventListener('click', function (evt) {
        loadRules(subjectEle.value, function (subjectRules) {
            var rules = mergeRules(baseRules, subjectRules);
            var tree = [];
            var rulesHTML = '';

            articleEle.innerHTML = cfg.expand('START', rules, tree);
            expansionEle.innerHTML = printExpansion(tree);

            if (prevSubject !== subject) {
                for (ruleName in rules) {
                    rulesHTML += rulesTemplate
                        .replace('{rule_name}', ruleName)
                        .replace('{values}',
                            rules[ruleName].map(function (value) {
                                return valuesTemplate.replace('{value}', value);
                            }).join('')
                        );
                }
                rulesEle.innerHTML = rulesHTML;
                prevSubject = subject;
            }

            resultsEle.style.display = 'block';
        });

        evt.preventDefault();
    });

    loadRules('base', function (rules) {
        baseRules = rules;
        submitEle.disabled = false;
    });
})();
