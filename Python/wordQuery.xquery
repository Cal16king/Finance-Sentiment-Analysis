declare variable $results := doc('results.xml');
declare variable $wordsOfInterest := ('inflation', 'market', 'rate', 'march', 'prices', 'tesla');

for $w in $wordsOfInterest
let $matches := $results//key[@name ! string()[contains(., $w)]]
let $count := count($matches)
let $dates := $matches/date
let $minDate := min($dates)
let $maxDate := max($dates)


    for $m in $matches
    let $article := $m/@name ! string()
    let $tokens := tokenize($article, ' ')[. = $w]
    let $countPerArticle := $tokens => count()
    let $dates := $m/date ! xs:date(.)
    where $countPerArticle > 0
    order by $dates descending
    return ($w || ': ' || $dates || ': '|| $countPerArticle || '&#10;')
    
(: ebb: This is not really properly organized to output the line graph you want for each word, but it helps to survey the data. :)