var cfg = (function () {
    var wsExp = /\s+/;
    var ntExp = /[A-Z][A-Z0-9_]*/g;

    function hasLength(x) {
        return x.length > 0;
    }

    function parse(s) {
        var rules = {};

        s.split('\n').forEach(function (line) {
            var toks = line.split(wsExp).filter(hasLength);
            if (toks.length > 0) {
                var ruleName = toks.shift();
                if (rules[ruleName] === undefined) {
                    rules[ruleName] = [];
                }
                rules[ruleName].push(toks.join(' '));
            }
        });

        return rules;
    }

    function expand(baseRule, rules) {
        return baseRule.replace(ntExp, function (ruleName) {
            var rule = rules[ruleName];
            if (rule !== undefined) {
                var i = Math.floor(Math.random() * rule.length);
                return expand(rule[i], rules);
            }
            return ruleName;
        });
    }

    return {
        'parse': parse,
        'expand': expand
    }
})();
