CREATE VIEW logarticleid AS
SELECT log.path,
       log.id,"substring"(log.path,10) as logslug,
       articles.id as articleid
    FROM log, articles
    WHERE '/article/' || articles.slug = log.path;

CREATE VIEW mostview AS
 SELECT articles.id,
    articles.title, 
    count(*) AS views    
   FROM articles,
    logarticleid
  WHERE articles.id = logarticleid.articleid
  GROUP BY articles.title, articles.id
  ORDER BY (count(*)) DESC
  LIMIT 3;

CREATE VIEW mostread AS
 SELECT mostview.id,
    mostview.views,
    articles.author,
    articles.title
   FROM mostview,
    articles
  WHERE mostview.id = articles.id;

CREATE VIEW errortype AS
SELECT date(log."time") AS date,
    log.status,
    count(*) AS type
   FROM log
  GROUP BY (date(log."time")), log.status; 

CREATE VIEW requestbad AS
SELECT errortype.date,
    errortype.status,
    errortype.type
   FROM errortype
  WHERE errortype.status = '404 NOT FOUND'::text;

CREATE VIEW totalhits AS
SELECT errortype.date,
    count(*) AS requesttype,
    sum(errortype.type) AS hits
  FROM errortype
 GROUP BY errortype.date;