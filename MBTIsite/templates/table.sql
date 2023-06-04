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

-- 테이블 eventdb.wh_event 구조 내보내기
DROP TABLE IF EXISTS `wh_event`;
CREATE TABLE IF NOT EXISTS `wh_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` varchar(50) DEFAULT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  `user_note` varchar(4096) DEFAULT NULL,
  `event_result` varchar(1024) DEFAULT NULL,
  `level_max` int(11) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;

-- 테이블 데이터 eventdb.wh_event:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wh_event` DISABLE KEYS */;
INSERT INTO `wh_event` (`id`, `event_id`, `user_answer`, `user_note`, `event_result`, `level_max`) VALUES
	(81, '2020-12-18 20:10:27.314760', '1.1.1.1.1.', 'Q1.E.1\r\nQ2.E.1.1\r\nQ3.E.1.1.1\r\nQ4.E.1.1.1.1\r\nQ5.E.1.1.1.1.1\r\n', '', 5);
/*!40000 ALTER TABLE `wh_event` ENABLE KEYS */;

-- 테이블 eventdb.wh_result 구조 내보내기
DROP TABLE IF EXISTS `wh_result`;
CREATE TABLE IF NOT EXISTS `wh_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `header_id` int(11) NOT NULL DEFAULT 0,
  `result_code` varchar(255) DEFAULT NULL,
  `result_link` varchar(1024) DEFAULT NULL,
  `image_link` varchar(1024) DEFAULT NULL,
  `result_desc` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- 테이블 데이터 eventdb.wh_result:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wh_result` DISABLE KEYS */;
INSERT INTO `wh_result` (`id`, `header_id`, `result_code`, `result_link`, `image_link`, `result_desc`) VALUES
	(6, 3, '1.1.1.1.1.', 'http://www.globalintelligence.kr/', '', '글로벌!!!');
/*!40000 ALTER TABLE `wh_result` ENABLE KEYS */;

-- 테이블 eventdb.wm_qheader 구조 내보내기
DROP TABLE IF EXISTS `wm_qheader`;
CREATE TABLE IF NOT EXISTS `wm_qheader` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(50) DEFAULT NULL,
  `pdesc` varchar(255) DEFAULT NULL,
  `level_max` int(11) DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 테이블 데이터 eventdb.wm_qheader:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wm_qheader` DISABLE KEYS */;
INSERT INTO `wm_qheader` (`id`, `pname`, `pdesc`, `level_max`) VALUES
	(3, 'E1', '연말이벤트', 5);
/*!40000 ALTER TABLE `wm_qheader` ENABLE KEYS */;

-- 테이블 eventdb.wm_question 구조 내보내기
DROP TABLE IF EXISTS `wm_question`;
CREATE TABLE IF NOT EXISTS `wm_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `header_id` int(11) DEFAULT 0,
  `parent_id` int(11) DEFAULT 0,
  `order_no` int(11) DEFAULT 1,
  `qlevel` int(11) DEFAULT 1,
  `qname` varchar(50) DEFAULT NULL,
  `qdesc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

-- 테이블 데이터 eventdb.wm_question:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wm_question` DISABLE KEYS */;
INSERT INTO `wm_question` (`id`, `header_id`, `parent_id`, `order_no`, `qlevel`, `qname`, `qdesc`) VALUES
	(31, 3, 0, 1, 1, '1.', '잘문 1 입니다.'),
	(32, 3, 0, 2, 1, '2.', '잘문 2 입니다.'),
	(33, 3, 0, 3, 1, '3.', '잘문 3 입니다.'),
	(34, 3, 31, 1, 2, '1.1.', '청바지로 멋내기'),
	(35, 3, 31, 2, 2, '1.2.', '정장 스똬일'),
	(36, 3, 31, 3, 2, '1.3.', '골프웨어로~~~'),
	(37, 3, 34, 1, 3, '1.1.1.', '대님에 비니?'),
	(38, 3, 34, 2, 3, '1.1.2.', '청자켓 매치~~~'),
	(39, 3, 34, 3, 3, '1.1.3.', '스니커즈 필수'),
	(40, 3, 37, 1, 4, '1.1.1.1.', '청과 붉은 탑'),
	(41, 3, 37, 2, 4, '1.1.1.2.', '청청의 조화'),
	(42, 3, 37, 3, 4, '1.1.1.3.', '흰색의 포인트'),
	(43, 3, 40, 1, 5, '1.1.1.1.1.', '중간은 노랑?'),
	(44, 3, 40, 2, 5, '1.1.1.1.2.', '흰색티의 중화'),
	(45, 3, 40, 3, 5, '1.1.1.1.3.', '색동으로 어울리자'),
	(46, 3, 0, 4, 1, '4.', '붉은색 좋아하세요?'),
	(47, 3, 46, 1, 2, '4.1.', '빨간 사과를 좋아 합니다.'),
	(48, 3, 46, 2, 2, '4.2.', '볼 빤간 사춘기가 좋아요!!!'),
	(49, 3, 46, 3, 2, '4.3.', '정열의 적도, 이글거리는 태양!'),
	(50, 3, 47, 1, 3, '4.1.1.', '가을 사과'),
	(51, 3, 47, 2, 3, '4.1.2.', '사과 잼'),
	(52, 3, 47, 3, 3, '4.1.3.', '사과 쥬스'),
	(53, 3, 50, 1, 4, '4.1.1.1.', '늦 가을에 안주!'),
	(54, 3, 50, 2, 4, '4.1.1.2.', '초 가을 과수원으로'),
	(55, 3, 50, 3, 4, '4.1.1.3.', '배달의 사과'),
	(56, 3, 53, 1, 5, '4.1.1.1.1.', '븕은 막걸리'),
	(57, 3, 53, 2, 5, '4.1.1.1.2.', '사과 쐬주!'),
	(58, 3, 53, 3, 5, '4.1.1.1.3.', '쥬스~~~');
/*!40000 ALTER TABLE `wm_question` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
