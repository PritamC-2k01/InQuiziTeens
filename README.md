# InQuiziTeens

Heads up Quizzers! 
We, at InQuiziTeens , bring you a fresh new website to satiate all your quizzing thirsts! We have a collection of 20 handpicked questions from a mixed bag with an overall moderate difficulty level to cater to all levels of our users.  Questions are updated weekly so don’t forget to check out every week. Login with your email today and play the quiz as many times as you want with no time limit at all.  We also hash the password you enter so only you know it. (Ahem)🌚
This website has been built from scratch all by ourselves. Please use the feedback option at the end of the quiz to let us know how we can improve. 

<b>Play the quiz here 🔽
https://quizing.epizy.com/index.php</b>

Wish you Happy Quzzing from all of us at InQuiziTeens.

For queries, mail to: inquiziteens@gmail.com



<h1>Moving Towards Coding</h1>

<h2>1 : Creating a MySQL Database for the project </h2> 

```sql
CREATE DATABASE quiz;
```
<h2>2 : Creating a User for the  database</h2>

```sql
    CREATE USER 'example'@localhost IDENTIFIED BY 'example';
    GRANT ALL ON workspace.* TO 'example'@localhost;
```
<h2>3: Creating All Tables</h2>

```sql
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(128) DEFAULT NULL,
  `pw` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `school` varchar(255) DEFAULT NULL,
  PRIMARY KEY(user_id)
);

CREATE TABLE `questions` (
  `qs_id` int(11) NOT NULL AUTO_INCREMENT,
  `qs` longtext,
  `option1` varchar(255) NOT NULL,
  `option2` varchar(255) NOT NULL,
  `option3` varchar(255) NOT NULL,
  `option4` varchar(255) NOT NULL,
  `ans` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY(qs_id)
);

CREATE TABLE `score` (
  `score_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `scores` int(11) DEFAULT NULL,
  PRIMARY KEY(score_id),
  
  CONSTRAINT FOREIGN KEY(user_id)
  REFERENCES users(user_id)
  ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE `feedback` (
  `fb_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `fb` varchar(255) DEFAULT NULL,
  PRIMARY KEY(fb_id),
  
  CONSTRAINT FOREIGN KEY(user_id)
  REFERENCES users(user_id)
  ON DELETE CASCADE ON UPDATE CASCADE
);
```
<h2>4: Inserting Questions, Options and Answer </h2>
```sql
INSERT INTO `questions` (`qs`, `option1`, `option2`, `option3`, `option4`, `ans`, `image`) VALUES ('YOUR QS 1','OPTION 1','OPTION 2','OPTION3',' OPTION4 ','ANSWER','IMAGE_URL');
```

<b> In the quiz.php file , please add your first question , options and answer at the mentioned line .</b>
