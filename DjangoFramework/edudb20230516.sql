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

-- 테이블 edudb.account_emailaddress 구조 내보내기
CREATE TABLE IF NOT EXISTS `account_emailaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.account_emailconfirmation 구조 내보내기
CREATE TABLE IF NOT EXISTS `account_emailconfirmation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.album 구조 내보내기
CREATE TABLE IF NOT EXISTS `album` (
  `a_no` int(11) NOT NULL AUTO_INCREMENT,
  `a_type` varchar(50) NOT NULL,
  `a_title` varchar(255) NOT NULL,
  `a_note` varchar(4096) DEFAULT NULL,
  `a_image` varchar(1024) DEFAULT NULL,
  `a_count` int(11) NOT NULL DEFAULT 0,
  `a_datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `a_usage` varchar(10) NOT NULL DEFAULT '1',
  PRIMARY KEY (`a_no`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.auth_group 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.auth_group_permissions 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.auth_permission 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.auth_user 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.auth_user_groups 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.auth_user_user_permissions 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.board 구조 내보내기
CREATE TABLE IF NOT EXISTS `board` (
  `b_no` int(11) NOT NULL AUTO_INCREMENT,
  `b_title` varchar(255) NOT NULL,
  `b_note` varchar(4096) DEFAULT NULL,
  `parent_no` int(11) DEFAULT 0,
  `b_writer` varchar(50) DEFAULT NULL,
  `b_count` int(11) DEFAULT 0,
  `b_date` timestamp NOT NULL DEFAULT curdate(),
  `usage_flag` varchar(10) DEFAULT '1',
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.board1 구조 내보내기
CREATE TABLE IF NOT EXISTS `board1` (
  `b_no` int(11) NOT NULL AUTO_INCREMENT,
  `b_title` varchar(255) DEFAULT NULL,
  `b_note` varchar(4096) DEFAULT NULL,
  `parnt_no` int(11) DEFAULT 0,
  `b_writer` varchar(50) DEFAULT NULL,
  `b_count` int(11) DEFAULT 0,
  `b_date` datetime DEFAULT NULL,
  `usage_flag` char(1) DEFAULT 'Y',
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.board2 구조 내보내기
CREATE TABLE IF NOT EXISTS `board2` (
  `b_no` int(11) NOT NULL AUTO_INCREMENT,
  `b_title` varchar(255) NOT NULL,
  `b_note` varchar(4096) DEFAULT NULL,
  `parent_no` int(11) DEFAULT 0,
  `b_writer` varchar(50) DEFAULT NULL,
  `b_count` int(11) DEFAULT 0,
  `b_date` datetime DEFAULT current_timestamp(),
  `usage_flag` varchar(10) DEFAULT '1',
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.board3 구조 내보내기
CREATE TABLE IF NOT EXISTS `board3` (
  `b_no` int(11) NOT NULL AUTO_INCREMENT,
  `b_title` varchar(255) DEFAULT NULL,
  `b_note` varchar(4096) DEFAULT NULL,
  `parent_no` int(11) DEFAULT 0,
  `b_writer` varchar(50) DEFAULT NULL,
  `b_count` int(11) DEFAULT 0,
  `b_date` datetime DEFAULT NULL,
  `usage_flag` char(1) DEFAULT 'Y',
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.boardimg 구조 내보내기
CREATE TABLE IF NOT EXISTS `boardimg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_title` varchar(255) DEFAULT '',
  `image_url` varchar(255) DEFAULT '',
  `image_file` mediumblob DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.boardnew 구조 내보내기
CREATE TABLE IF NOT EXISTS `boardnew` (
  `b_no` int(11) NOT NULL AUTO_INCREMENT,
  `b_title` varchar(255) NOT NULL,
  `b_note` varchar(4096) DEFAULT NULL,
  `type_id` int(11) DEFAULT 1,
  `parent_no` int(11) DEFAULT 0,
  `b_writer` varchar(50) DEFAULT NULL,
  `b_count` int(11) DEFAULT 0,
  `b_date` timestamp NOT NULL DEFAULT curdate(),
  `usage_flag` varchar(10) DEFAULT '1',
  PRIMARY KEY (`b_no`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.boardtype 구조 내보내기
CREATE TABLE IF NOT EXISTS `boardtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cb_code_dtl 구조 내보내기
CREATE TABLE IF NOT EXISTS `cb_code_dtl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_cd` varchar(20) DEFAULT NULL,
  `code_cd` varchar(20) DEFAULT NULL,
  `code_name` varchar(50) DEFAULT NULL,
  `register_date` timestamp NULL DEFAULT current_timestamp(),
  `usage_flag` varchar(10) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cb_code_hdr 구조 내보내기
CREATE TABLE IF NOT EXISTS `cb_code_hdr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_cd` varchar(20) DEFAULT NULL,
  `type_name` varchar(50) DEFAULT NULL,
  `register_date` timestamp NULL DEFAULT current_timestamp(),
  `usage_flag` varchar(10) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cb_itemgrp 구조 내보내기
CREATE TABLE IF NOT EXISTS `cb_itemgrp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemgrp_cd` varchar(20) DEFAULT NULL,
  `itemgrp_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cm_bom 구조 내보내기
CREATE TABLE IF NOT EXISTS `cm_bom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bom_type` varchar(20) DEFAULT 'MBOM',
  `item_id` int(11) DEFAULT 0,
  `top_id` int(11) DEFAULT 0,
  `parent_id` int(11) DEFAULT 0,
  `bom_order` int(11) DEFAULT 1,
  `bom_level` int(11) DEFAULT 1,
  `leaf_flag` varchar(10) DEFAULT '1',
  `moitem_base` float DEFAULT 0,
  `jaitem_base` float DEFAULT 0,
  `unit_product` varchar(20) DEFAULT NULL,
  `free_flag` varchar(10) DEFAULT '0',
  `loss_product` float DEFAULT 0,
  `demand_amt` float DEFAULT 0,
  `start_date` varchar(8) DEFAULT NULL,
  `end_date` varchar(8) DEFAULT NULL,
  `register_date` datetime DEFAULT NULL,
  `usage_flag` varchar(8) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cm_factory 구조 내보내기
CREATE TABLE IF NOT EXISTS `cm_factory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `factory_cd` varchar(20) DEFAULT NULL,
  `factory_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cm_item 구조 내보내기
CREATE TABLE IF NOT EXISTS `cm_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `factory_id` int(11) DEFAULT 0,
  `itemgrp_id` int(11) DEFAULT 0,
  `itemaccnt_id` int(11) DEFAULT 0,
  `unit_id` int(11) DEFAULT 0,
  `item_cd` varchar(20) NOT NULL,
  `item_name` varchar(50) DEFAULT NULL,
  `item_spec` varchar(255) DEFAULT NULL,
  `item_status` varchar(10) DEFAULT 'Active',
  `register_date` datetime DEFAULT current_timestamp(),
  `usage_flag` varchar(10) DEFAULT '1',
  `bom_flag` varchar(10) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.cm_itemaccnt 구조 내보내기
CREATE TABLE IF NOT EXISTS `cm_itemaccnt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemaccnt_cd` varchar(20) DEFAULT NULL,
  `itemaccnt_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.config 구조 내보내기
CREATE TABLE IF NOT EXISTS `config` (
  `variable` varchar(30) NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`variable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.django_admin_log 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.django_content_type 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.django_migrations 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.django_session 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.django_site 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.entity1 구조 내보내기
CREATE TABLE IF NOT EXISTS `entity1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Col001` varchar(255) DEFAULT NULL,
  `Col002` varchar(255) DEFAULT NULL,
  `Col003` int(11) DEFAULT NULL,
  `Col004` int(11) DEFAULT NULL,
  `Col005` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.entity2 구조 내보내기
CREATE TABLE IF NOT EXISTS `entity2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Col001` varchar(255) DEFAULT NULL,
  `Col002` varchar(255) DEFAULT NULL,
  `Col003` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.entity4 구조 내보내기
CREATE TABLE IF NOT EXISTS `entity4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Col001` varchar(255) DEFAULT NULL,
  `Col002` varchar(255) DEFAULT NULL,
  `Col003` varchar(255) DEFAULT NULL,
  `Col004` int(11) DEFAULT NULL,
  `Col005` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.facedata 구조 내보내기
CREATE TABLE IF NOT EXISTS `facedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `detect_id` varchar(255) DEFAULT '1610592192893',
  `detect_date` datetime DEFAULT NULL,
  `detect_type` varchar(20) DEFAULT NULL,
  `device_id` varchar(20) DEFAULT 'D001',
  `user_no` varchar(50) DEFAULT NULL,
  `register_date` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.inventory2009 구조 내보내기
CREATE TABLE IF NOT EXISTS `inventory2009` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bsnscd` varchar(255) DEFAULT NULL,
  `measures` varchar(255) DEFAULT NULL,
  `yyyymmdd` varchar(255) DEFAULT NULL,
  `inv_init` int(11) DEFAULT NULL,
  `inv_close` int(11) DEFAULT NULL,
  `inv_input` int(11) DEFAULT NULL,
  `inv_output` int(11) DEFAULT NULL,
  `inv_rate` float DEFAULT NULL,
  `invrate_predict` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.keys 구조 내보내기
CREATE TABLE IF NOT EXISTS `keys` (
  `id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(80) DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `depth` int(11) DEFAULT NULL,
  `change` int(11) DEFAULT NULL,
  `address_index` bigint(20) DEFAULT NULL,
  `public` varbinary(128) DEFAULT NULL,
  `private` varbinary(128) DEFAULT NULL,
  `wif` varchar(255) DEFAULT NULL,
  `compressed` tinyint(1) DEFAULT NULL,
  `key_type` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `cosigner_id` int(11) DEFAULT NULL,
  `encoding` varchar(15) DEFAULT NULL,
  `purpose` int(11) DEFAULT NULL,
  `is_private` tinyint(1) DEFAULT NULL,
  `path` varchar(100) DEFAULT NULL,
  `wallet_id` int(11) DEFAULT NULL,
  `balance` bigint(20) DEFAULT NULL,
  `used` tinyint(1) DEFAULT NULL,
  `network_name` varchar(20) DEFAULT NULL,
  `latest_txid` varbinary(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `constraint_wallet_pubkey_unique` (`wallet_id`,`public`),
  UNIQUE KEY `constraint_wallet_privkey_unique` (`wallet_id`,`private`),
  UNIQUE KEY `constraint_wallet_wif_unique` (`wallet_id`,`wif`),
  UNIQUE KEY `constraint_wallet_address_unique` (`wallet_id`,`address`),
  KEY `network_name` (`network_name`),
  KEY `ix_keys_private` (`private`),
  KEY `ix_keys_wif` (`wif`),
  KEY `ix_keys_wallet_id` (`wallet_id`),
  KEY `ix_keys_address` (`address`),
  KEY `ix_keys_account_id` (`account_id`),
  KEY `ix_keys_public` (`public`),
  KEY `ix_keys_name` (`name`),
  CONSTRAINT `keys_ibfk_1` FOREIGN KEY (`wallet_id`) REFERENCES `wallets` (`id`),
  CONSTRAINT `keys_ibfk_2` FOREIGN KEY (`network_name`) REFERENCES `networks` (`name`),
  CONSTRAINT `constraint_key_types_allowed` CHECK (`key_type` in ('single','bip32','multisig')),
  CONSTRAINT `constraint_address_encodings_allowed` CHECK (`encoding` in ('base58','bech32'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.key_id_seq 구조 내보내기
CREATE TABLE IF NOT EXISTS `key_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) unsigned NOT NULL,
  `cycle_option` tinyint(1) unsigned NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB SEQUENCE=1;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.key_multisig_children 구조 내보내기
CREATE TABLE IF NOT EXISTS `key_multisig_children` (
  `parent_id` int(11) NOT NULL,
  `child_id` int(11) NOT NULL,
  `key_order` int(11) DEFAULT NULL,
  PRIMARY KEY (`parent_id`,`child_id`),
  KEY `child_id` (`child_id`),
  CONSTRAINT `key_multisig_children_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `keys` (`id`),
  CONSTRAINT `key_multisig_children_ibfk_2` FOREIGN KEY (`child_id`) REFERENCES `keys` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.key_multisig_children_id_seq 구조 내보내기
CREATE TABLE IF NOT EXISTS `key_multisig_children_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) unsigned NOT NULL,
  `cycle_option` tinyint(1) unsigned NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB SEQUENCE=1;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.member 구조 내보내기
CREATE TABLE IF NOT EXISTS `member` (
  `member_no` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` varchar(50) NOT NULL,
  `member_email` varchar(255) NOT NULL,
  `member_pwd` varchar(255) NOT NULL,
  `member_phone` varchar(255) DEFAULT '',
  `member_name` varchar(50) DEFAULT '',
  `usage_flag` varchar(10) DEFAULT NULL,
  `register_date` datetime DEFAULT current_timestamp(),
  `access_latest` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`member_no`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_board 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_board` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `b_title` varchar(255) DEFAULT NULL,
  `b_writer` varchar(50) DEFAULT NULL,
  `b_date` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_book 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `publication_date` date DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `pages` int(11) DEFAULT NULL,
  `book_type` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_city 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `timezone` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_entity 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_entity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entity_name` varchar(50) DEFAULT NULL,
  `status` varchar(10) DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_entityold 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_entityold` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entity_name` varchar(50) DEFAULT NULL,
  `status` varchar(10) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_meta 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_meta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entity_id` int(11) DEFAULT NULL,
  `column_name` varchar(50) DEFAULT NULL,
  `column_type` varchar(20) DEFAULT NULL,
  `column_length` int(11) DEFAULT NULL,
  `order_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_metaold 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_metaold` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entity_id` int(11) DEFAULT NULL,
  `column_name` varchar(50) DEFAULT NULL,
  `column_type` varchar(20) DEFAULT NULL,
  `column_length` int(11) DEFAULT NULL,
  `order_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.myapp_product 구조 내보내기
CREATE TABLE IF NOT EXISTS `myapp_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `productcode` varchar(10) DEFAULT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `category_type` smallint(6) DEFAULT NULL,
  `dateadded` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.networks 구조 내보내기
CREATE TABLE IF NOT EXISTS `networks` (
  `name` varchar(20) NOT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.parent_id_seq 구조 내보내기
CREATE TABLE IF NOT EXISTS `parent_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) unsigned NOT NULL,
  `cycle_option` tinyint(1) unsigned NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB SEQUENCE=1;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.pd_config 구조 내보내기
CREATE TABLE IF NOT EXISTS `pd_config` (
  `id` int(11) NOT NULL DEFAULT 1,
  `configtype` varchar(20) DEFAULT NULL,
  `configvalue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.pd_detectdata 구조 내보내기
CREATE TABLE IF NOT EXISTS `pd_detectdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `detected_at` datetime DEFAULT current_timestamp(),
  `device_id` varchar(20) DEFAULT 'D001',
  `frame_cnt` float DEFAULT NULL,
  `eye_rate` float DEFAULT NULL,
  `angle_yaw` int(11) DEFAULT NULL,
  `angle_pitch` int(11) DEFAULT NULL,
  `angle_roll` int(11) DEFAULT NULL,
  `image_name` varchar(255) DEFAULT '',
  `detect_fcnt` varchar(50) DEFAULT NULL,
  `detect_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=138 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.pd_device 구조 내보내기
CREATE TABLE IF NOT EXISTS `pd_device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `device_name` varchar(50) DEFAULT NULL,
  `lecation_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.pd_facedata 구조 내보내기
CREATE TABLE IF NOT EXISTS `pd_facedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `detect_id` varchar(255) DEFAULT '1610592192893',
  `detect_date` datetime DEFAULT NULL,
  `detect_type` varchar(20) DEFAULT NULL,
  `device_id` varchar(20) DEFAULT 'D001',
  `d_index` varchar(255) DEFAULT 'D001',
  `c_index` int(11) DEFAULT NULL,
  `user_no` varchar(50) DEFAULT NULL,
  `register_date` datetime DEFAULT current_timestamp(),
  `frame_cnt` float DEFAULT NULL,
  `state_left` float DEFAULT NULL,
  `state_right` float DEFAULT NULL,
  `angle_yaw` int(11) DEFAULT NULL,
  `angle_pitch` int(11) DEFAULT NULL,
  `angle_roll` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.pd_user 구조 내보내기
CREATE TABLE IF NOT EXISTS `pd_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `user_pwd` varchar(50) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `eyeopen_rate` float DEFAULT NULL,
  `eyeclose_rate` float DEFAULT NULL,
  `yaw_start` int(11) DEFAULT NULL,
  `yaw_end` int(11) DEFAULT NULL,
  `pitch_start` int(11) DEFAULT NULL,
  `pitch_end` int(11) DEFAULT NULL,
  `roll_start` int(11) DEFAULT NULL,
  `roll_end` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.person 구조 내보내기
CREATE TABLE IF NOT EXISTS `person` (
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.sales_predict 구조 내보내기
CREATE TABLE IF NOT EXISTS `sales_predict` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `yyyymm` varchar(20) DEFAULT NULL,
  `sales_amt` int(11) DEFAULT NULL,
  `sales_predict` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.socialaccount_socialaccount 구조 내보내기
CREATE TABLE IF NOT EXISTS `socialaccount_socialaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.socialaccount_socialapp 구조 내보내기
CREATE TABLE IF NOT EXISTS `socialaccount_socialapp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.socialaccount_socialapp_sites 구조 내보내기
CREATE TABLE IF NOT EXISTS `socialaccount_socialapp_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.socialaccount_socialtoken 구조 내보내기
CREATE TABLE IF NOT EXISTS `socialaccount_socialtoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.transactions 구조 내보내기
CREATE TABLE IF NOT EXISTS `transactions` (
  `id` int(11) NOT NULL,
  `txid` varbinary(32) DEFAULT NULL,
  `wallet_id` int(11) DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `witness_type` varchar(20) DEFAULT NULL,
  `version` bigint(20) DEFAULT NULL,
  `locktime` bigint(20) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `coinbase` tinyint(1) DEFAULT NULL,
  `confirmations` int(11) DEFAULT NULL,
  `block_height` int(11) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `fee` bigint(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `is_complete` tinyint(1) DEFAULT NULL,
  `input_total` bigint(20) DEFAULT NULL,
  `output_total` bigint(20) DEFAULT NULL,
  `network_name` varchar(20) DEFAULT NULL,
  `raw` blob DEFAULT NULL,
  `verified` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `constraint_wallet_transaction_hash_unique` (`wallet_id`,`txid`),
  KEY `network_name` (`network_name`),
  KEY `ix_transactions_block_height` (`block_height`),
  KEY `ix_transactions_account_id` (`account_id`),
  KEY `ix_transactions_txid` (`txid`),
  KEY `ix_transactions_wallet_id` (`wallet_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`wallet_id`) REFERENCES `wallets` (`id`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`network_name`) REFERENCES `networks` (`name`),
  CONSTRAINT `constraint_status_allowed` CHECK (`status` in ('new','unconfirmed','confirmed')),
  CONSTRAINT `transaction_constraint_allowed_types` CHECK (`witness_type` in ('legacy','segwit'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.transaction_id_seq 구조 내보내기
CREATE TABLE IF NOT EXISTS `transaction_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) unsigned NOT NULL,
  `cycle_option` tinyint(1) unsigned NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB SEQUENCE=1;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.transaction_inputs 구조 내보내기
CREATE TABLE IF NOT EXISTS `transaction_inputs` (
  `transaction_id` int(11) NOT NULL,
  `index_n` int(11) NOT NULL,
  `key_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `witnesses` blob DEFAULT NULL,
  `witness_type` varchar(20) DEFAULT NULL,
  `prev_txid` varbinary(32) DEFAULT NULL,
  `output_n` bigint(20) DEFAULT NULL,
  `script` blob DEFAULT NULL,
  `script_type` varchar(20) DEFAULT NULL,
  `sequence` bigint(20) DEFAULT NULL,
  `value` bigint(20) DEFAULT NULL,
  `double_spend` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`,`index_n`),
  UNIQUE KEY `constraint_transaction_input_unique` (`transaction_id`,`index_n`),
  KEY `ix_transaction_inputs_key_id` (`key_id`),
  CONSTRAINT `transaction_inputs_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`id`),
  CONSTRAINT `transaction_inputs_ibfk_2` FOREIGN KEY (`key_id`) REFERENCES `keys` (`id`),
  CONSTRAINT `transactioninput_constraint_script_types_allowed` CHECK (`script_type` in ('','coinbase','sig_pubkey','p2sh_multisig','signature','unknown','p2sh_p2wpkh','p2sh_p2wsh')),
  CONSTRAINT `transactioninput_constraint_allowed_types` CHECK (`witness_type` in ('legacy','segwit','p2sh-segwit'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.transaction_outputs 구조 내보내기
CREATE TABLE IF NOT EXISTS `transaction_outputs` (
  `transaction_id` int(11) NOT NULL,
  `output_n` int(11) NOT NULL,
  `key_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `script` blob DEFAULT NULL,
  `script_type` varchar(20) DEFAULT NULL,
  `value` bigint(20) DEFAULT NULL,
  `spent` tinyint(1) DEFAULT NULL,
  `spending_txid` varbinary(32) DEFAULT NULL,
  `spending_index_n` int(11) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`,`output_n`),
  UNIQUE KEY `constraint_transaction_output_unique` (`transaction_id`,`output_n`),
  KEY `ix_transaction_outputs_key_id` (`key_id`),
  CONSTRAINT `transaction_outputs_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`id`),
  CONSTRAINT `transaction_outputs_ibfk_2` FOREIGN KEY (`key_id`) REFERENCES `keys` (`id`),
  CONSTRAINT `transactionoutput_constraint_script_types_allowed` CHECK (`script_type` in ('','p2pkh','multisig','p2sh','p2pk','nulldata','unknown','p2wpkh','p2wsh'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.user 구조 내보내기
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.wallets 구조 내보내기
CREATE TABLE IF NOT EXISTS `wallets` (
  `id` int(11) NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `network_name` varchar(20) DEFAULT NULL,
  `purpose` int(11) DEFAULT NULL,
  `scheme` varchar(25) DEFAULT NULL,
  `witness_type` varchar(20) DEFAULT NULL,
  `encoding` varchar(15) DEFAULT NULL,
  `main_key_id` int(11) DEFAULT NULL,
  `multisig_n_required` int(11) DEFAULT NULL,
  `sort_keys` tinyint(1) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `multisig` tinyint(1) DEFAULT NULL,
  `cosigner_id` int(11) DEFAULT NULL,
  `key_path` varchar(100) DEFAULT NULL,
  `default_account_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `network_name` (`network_name`),
  KEY `parent_id` (`parent_id`),
  CONSTRAINT `wallets_ibfk_1` FOREIGN KEY (`network_name`) REFERENCES `networks` (`name`),
  CONSTRAINT `wallets_ibfk_2` FOREIGN KEY (`parent_id`) REFERENCES `wallets` (`id`),
  CONSTRAINT `constraint_allowed_schemes` CHECK (`scheme` in ('single','bip32')),
  CONSTRAINT `constraint_default_address_encodings_allowed` CHECK (`encoding` in ('base58','bech32')),
  CONSTRAINT `wallet_constraint_allowed_types` CHECK (`witness_type` in ('legacy','segwit','p2sh-segwit'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.wallet_id_seq 구조 내보내기
CREATE TABLE IF NOT EXISTS `wallet_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) unsigned NOT NULL,
  `cycle_option` tinyint(1) unsigned NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB SEQUENCE=1;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.weblog 구조 내보내기
CREATE TABLE IF NOT EXISTS `weblog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_no` int(11) NOT NULL DEFAULT 0,
  `server_desc` varchar(255) DEFAULT NULL,
  `useragent` varchar(255) DEFAULT NULL,
  `url_desc` varchar(255) DEFAULT NULL,
  `log_date` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 edudb.weblog_url 구조 내보내기
CREATE TABLE IF NOT EXISTS `weblog_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_desc` varchar(255) DEFAULT NULL,
  `yyyymmdd` varchar(8) DEFAULT NULL,
  `click_cnt` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
