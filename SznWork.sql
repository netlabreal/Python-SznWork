-- --------------------------------------------------------
-- Хост:                         192.168.1.100
-- Версия сервера:               5.5.44-0ubuntu0.14.04.1 - (Ubuntu)
-- ОС Сервера:                   debian-linux-gnu
-- HeidiSQL Версия:              9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Дамп структуры базы данных for_szn
CREATE DATABASE IF NOT EXISTS `for_szn` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `for_szn`;


-- Дамп структуры для таблица for_szn.months
CREATE TABLE IF NOT EXISTS `months` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` date NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.


-- Дамп структуры для таблица for_szn.oborots
CREATE TABLE IF NOT EXISTS `oborots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ls` int(11) NOT NULL DEFAULT '0',
  `month` int(11) NOT NULL DEFAULT '0',
  `usl` int(11) NOT NULL DEFAULT '0',
  `tarif` double NOT NULL DEFAULT '0',
  `vx` double NOT NULL DEFAULT '0',
  `nach` double NOT NULL DEFAULT '0',
  `vist` double NOT NULL DEFAULT '0',
  `opl` double NOT NULL DEFAULT '0',
  `isx` double NOT NULL DEFAULT '0',
  `plosh` double NOT NULL DEFAULT '0',
  `prop` int(11) NOT NULL DEFAULT '0',
  `org` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_oborots_months` (`month`),
  KEY `FK_oborots_uslugi` (`usl`),
  KEY `FK_oborots_our_ls` (`ls`),
  KEY `FK_oborots_organizations` (`org`),
  CONSTRAINT `FK_oborots_months` FOREIGN KEY (`month`) REFERENCES `months` (`id`),
  CONSTRAINT `FK_oborots_organizations` FOREIGN KEY (`org`) REFERENCES `organizations` (`id`),
  CONSTRAINT `FK_oborots_our_ls` FOREIGN KEY (`ls`) REFERENCES `our_ls` (`id`),
  CONSTRAINT `FK_oborots_uslugi` FOREIGN KEY (`usl`) REFERENCES `uslugi` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.


-- Дамп структуры для таблица for_szn.organizations
CREATE TABLE IF NOT EXISTS `organizations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.


-- Дамп структуры для таблица for_szn.our_ls
CREATE TABLE IF NOT EXISTS `our_ls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomer` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `nomer` (`nomer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.


-- Дамп структуры для таблица for_szn.szn_ls
CREATE TABLE IF NOT EXISTS `szn_ls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pku` varchar(12) NOT NULL,
  `adr` varchar(150) DEFAULT NULL,
  `ls` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pku` (`pku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.


-- Дамп структуры для таблица for_szn.szn_uslugi
CREATE TABLE IF NOT EXISTS `szn_uslugi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL DEFAULT '0',
  `usl_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.


-- Дамп структуры для таблица for_szn.uslugi
CREATE TABLE IF NOT EXISTS `uslugi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
