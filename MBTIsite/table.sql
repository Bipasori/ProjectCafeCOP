-- --------------------------------------------------------
-- 호스트:                          223.194.46.212
-- 서버 버전:                        10.4.6-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 테이블 winedb.wh_event 구조 내보내기
CREATE TABLE IF NOT EXISTS `wh_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` varchar(50) DEFAULT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  `user_note` varchar(4096) DEFAULT NULL,
  `event_result` varchar(1024) DEFAULT NULL,
  `level_max` int(11) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;

-- 테이블 데이터 winedb.wh_event:~50 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wh_event` DISABLE KEYS */;
REPLACE INTO `wh_event` (`id`, `event_id`, `user_answer`, `user_note`, `event_result`, `level_max`) VALUES
	(1, '2020-12-16 16:53:29.301199', '', NULL, '', 1),
	(2, '2020-12-16 16:54:51.824036', '', NULL, '', 1),
	(3, '2020-12-16 16:58:29.732262', '', NULL, '', 1),
	(4, '2020-12-16 16:59:14.080470', '', NULL, '', 1),
	(5, '2020-12-16 16:59:21.131966', '', NULL, '', 1),
	(6, '2020-12-16 16:59:58.566477', '', NULL, '', 1),
	(7, '2020-12-16 17:00:03.799276', '', NULL, '', 1),
	(8, '2020-12-16 17:00:08.642547', '', NULL, '', 1),
	(9, '2020-12-16 17:16:49.702284', '.1.1', NULL, '', 1),
	(10, '2020-12-16 17:17:07.261045', '.1', NULL, '', 1),
	(11, '2020-12-16 17:17:39.144294', '1.1.', NULL, '', 1),
	(12, '2020-12-16 17:44:46.952791', '1.1.', NULL, '', 1),
	(13, '2020-12-16 23:17:23.772390', '1.1.1.1.1.1.1.', NULL, '', 1),
	(14, '2020-12-16 23:48:34.130114', '1.1.1.1.1.1.1.', NULL, '', 1),
	(15, '2020-12-16 23:58:47.428803', '1.1.1.1.1.1.1.', NULL, '', 7),
	(16, '2020-12-17 00:04:46.710961', '1.1.1.1.1.1.1.', NULL, '', 7),
	(17, '2020-12-17 00:11:01.014953', '', '', '', 7),
	(18, '2020-12-17 00:11:41.097788', '1.1.1.1.1.1.1.', '<div>Q1.연인과 데이트</div><br><div>Q2.역시 레스토랑!</div><br><div>Q3.일편단심 Red</div><br><div>Q4.유럽의 전통</div><br><div>Q5.프랑스의 자유로움</div><br><div>Q6.오래된 향기</div><br><div>Q7.정열의 두잔!!!</div><br>', '', 7),
	(19, '2020-12-17 00:14:27.332903', '1.', '<div>Q1.연인과 데이트</div>', '', 7),
	(20, '2020-12-17 00:17:31.558317', '', '', '', 7),
	(21, '2020-12-17 00:17:36.157055', '1.1.1.1.1.1.1.', '<div>Q1.연인과 데이트</div><div>Q2.역시 레스토랑!</div><div>Q3.일편단심 Red</div><div>Q4.유럽의 전통</div><div>Q5.프랑스의 자유로움</div><div>Q6.오래된 향기</div><div>Q7.정열의 두잔!!!</div>', '', 7),
	(22, '2020-12-17 00:19:12.274006', '', '', '', 7),
	(23, '2020-12-17 00:19:24.920395', '1.1.1.1.1.1.1.', '<div>Q1.연인과 데이트</div><br><div>Q2.역시 레스토랑!</div><br><div>Q3.일편단심 Red</div><br><div>Q4.유럽의 전통</div><br><div>Q5.프랑스의 자유로움</div><br><div>Q6.오래된 향기</div><br><div>Q7.정열의 두잔!!!</div><br>', '', 7),
	(24, '2020-12-17 00:23:24.486332', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\nQ2.역시 레스토랑!\nQ3.일편단심 Red\nQ4.유럽의 전통\nQ5.프랑스의 자유로움\nQ6.오래된 향기\nQ7.정열의 두잔!!!\n', '', 7),
	(25, '2020-12-17 00:23:57.591465', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(26, '2020-12-17 00:25:43.770963', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(27, '2020-12-17 00:27:05.575703', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(28, '2020-12-17 00:30:26.862409', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(29, '2020-12-17 00:32:44.229738', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(30, '2020-12-17 00:33:07.312716', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(31, '2020-12-17 00:34:21.507276', '1.', 'Q1.연인과 데이트\r\n', '', 7),
	(32, '2020-12-17 00:35:44.574579', '1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\n', '', 7),
	(33, '2020-12-17 00:37:36.878960', '', '', '', 7),
	(34, '2020-12-17 00:38:01.920077', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(35, '2020-12-17 00:39:38.547641', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(36, '2020-12-17 00:40:35.356810', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(37, '2020-12-17 00:42:18.430688', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(38, '2020-12-17 00:54:24.076264', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(39, '2020-12-17 00:54:34.886539', '1.1.1.1.1.1.2.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.둘이서 한병\r\n', '', 7),
	(40, '2020-12-17 00:57:11.310512', '', '', '', 7),
	(41, '2020-12-17 00:57:19.637233', '', '', '', 7),
	(42, '2020-12-17 00:58:05.703028', '', '', '', 7),
	(43, '2020-12-17 00:58:11.505908', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(44, '2020-12-17 01:01:29.111572', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(45, '2020-12-17 01:04:01.491696', '1.1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(46, '2020-12-17 01:05:33.214324', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(47, '2020-12-17 01:16:20.099406', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(48, '2020-12-17 01:22:36.882139', '1.1.1.1.1.1.1.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.정열의 두잔!!!\r\n', '', 7),
	(49, '2020-12-17 01:22:46.205271', '1.1.1.1.1.3.1.3.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.AI의 코끝!\r\nQ6.오래된 향기\r\nQ7.친구들과 한짝\r\n', '', 7),
	(50, '2020-12-17 02:02:44.627009', '1.1.1.1.1.1.3.', 'Q1.연인과 데이트\r\nQ2.역시 레스토랑!\r\nQ3.일편단심 Red\r\nQ4.유럽의 전통\r\nQ5.프랑스의 자유로움\r\nQ6.오래된 향기\r\nQ7.친구들과 한짝\r\n', '', 7);
/*!40000 ALTER TABLE `wh_event` ENABLE KEYS */;

-- 테이블 winedb.wh_result 구조 내보내기
CREATE TABLE IF NOT EXISTS `wh_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `header_id` int(11) NOT NULL DEFAULT 0,
  `result_code` varchar(255) DEFAULT NULL,
  `result_link` varchar(1024) DEFAULT NULL,
  `image_link` varchar(1024) DEFAULT NULL,
  `result_desc` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 테이블 데이터 winedb.wh_result:~5 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wh_result` DISABLE KEYS */;
REPLACE INTO `wh_result` (`id`, `header_id`, `result_code`, `result_link`, `image_link`, `result_desc`) VALUES
	(1, 1, '1.1.1.1.1.1.1.', 'https://www.google.com/search?q=white%20wine', 'https://www.mdanderson.org/publications/focused-on-health/February-2017/red-wine-health-benefits-facts-and-myths/jcr:content/featuredImage.resize.1444.0.medium.dir.jpg/1542758649561.jpg', '깔끔한 화이트.'),
	(2, 1, '1.1.1.1.1.1.2.', 'https://www.google.com/search?q=red%20wine', 'https://www.mdanderson.org/publications/focused-on-health/February-2017/red-wine-health-benefits-facts-and-myths/jcr:content/featuredImage.resize.1444.0.medium.dir.jpg/1542758649561.jpg', '암거나 짱!'),
	(3, 1, '1.1.1.1.1.1.3.', 'https://www.google.com/search?q=red%20wine%20cabinet', 'https://www.mdanderson.org/publications/focused-on-health/February-2017/red-wine-health-benefits-facts-and-myths/jcr:content/featuredImage.resize.1444.0.medium.dir.jpg/1542758649561.jpg', '와인 저장고가 필요해!'),
	(4, 1, '1.1.1.1.1.1.1.', 'http://www.globalintelligence.kr/', 'https://www.mdanderson.org/publications/focused-on-health/February-2017/red-wine-health-benefits-facts-and-myths/jcr:content/featuredImage.resize.1444.0.medium.dir.jpg/1542758649561.jpg', '역쉬 레드!'),
	(5, 1, '1.1.1.1.1.1.3.', 'https://www.google.com/search?q=red wine', 'https://www.mdanderson.org/publications/focused-on-health/February-2017/red-wine-health-benefits-facts-and-myths/jcr:content/featuredImage.resize.1444.0.medium.dir.jpg/1542758649561.jpg', '칭구들과 레드!');
/*!40000 ALTER TABLE `wh_result` ENABLE KEYS */;

-- 테이블 winedb.wm_qheader 구조 내보내기
CREATE TABLE IF NOT EXISTS `wm_qheader` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(50) DEFAULT NULL,
  `pdesc` varchar(255) DEFAULT NULL,
  `level_max` int(11) DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 테이블 데이터 winedb.wm_qheader:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wm_qheader` DISABLE KEYS */;
REPLACE INTO `wm_qheader` (`id`, `pname`, `pdesc`, `level_max`) VALUES
	(1, 'Year12', '이번 연말 꼭 하고 싶은 것은 무엇인가요?', 7),
	(2, 'Year01', '새해 맞이 뭐 하실래요?', 1);
/*!40000 ALTER TABLE `wm_qheader` ENABLE KEYS */;

-- 테이블 winedb.wm_question 구조 내보내기
CREATE TABLE IF NOT EXISTS `wm_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `header_id` int(11) DEFAULT 0,
  `parent_id` int(11) DEFAULT 0,
  `order_no` int(11) DEFAULT 1,
  `qlevel` int(11) DEFAULT 1,
  `qname` varchar(50) DEFAULT NULL,
  `qdesc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- 테이블 데이터 winedb.wm_question:~24 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wm_question` DISABLE KEYS */;
REPLACE INTO `wm_question` (`id`, `header_id`, `parent_id`, `order_no`, `qlevel`, `qname`, `qdesc`) VALUES
	(5, 1, 0, 1, 1, 'Q1', '연인과 데이트'),
	(6, 1, 0, 1, 1, 'Q1', '가족과 저녁식사'),
	(7, 1, 0, 1, 1, 'Q1', '친구들과 연말 파티'),
	(8, 1, 0, 1, 1, 'Q1', '집에서 혼술'),
	(9, 1, 5, 1, 2, 'Q2', '역시 레스토랑!'),
	(10, 1, 5, 1, 2, 'Q2', '아늑하게 호캉스!'),
	(11, 1, 6, 1, 2, 'Q2', '외식이다!'),
	(12, 1, 6, 1, 2, 'Q2', '집에서 먹자'),
	(13, 1, 6, 1, 2, 'Q2', '제주도 가자,'),
	(14, 2, 0, 1, 1, 'Child...', 'Child...'),
	(15, 1, 11, 1, 3, 'Q3', 'Child...'),
	(16, 1, 11, 2, 3, 'Q3', 'Child...'),
	(17, 1, 9, 1, 3, 'Q3', '일편단심 Red'),
	(18, 1, 9, 2, 3, 'Q3', '화이트의 깨끗함!'),
	(19, 1, 17, 1, 4, 'Q4', '유럽의 전통'),
	(20, 1, 17, 2, 4, 'Q4', '남미의 햇살'),
	(21, 1, 19, 1, 5, 'Q5', '프랑스의 자유로움'),
	(22, 1, 19, 2, 5, 'Q5', '독일의 견고함'),
	(23, 1, 21, 1, 6, 'Q6', '오래된 향기'),
	(24, 1, 21, 2, 6, 'Q6', '케미 폭발 새로움~~~'),
	(25, 1, 23, 1, 7, 'Q7', '정열의 두잔!!!'),
	(26, 1, 23, 2, 7, 'Q7', '둘이서 한병'),
	(27, 1, 21, 3, 6, 'Q6', 'AI의 코끝!'),
	(28, 1, 23, 3, 7, 'Q7', '친구들과 한짝');
/*!40000 ALTER TABLE `wm_question` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
