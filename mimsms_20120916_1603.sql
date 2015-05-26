-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.63-0+squeeze1


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema mimsms
--

CREATE DATABASE IF NOT EXISTS mimsms;
USE mimsms;

--
-- Definition of table `mimsms`.`agenda`
--

DROP TABLE IF EXISTS `mimsms`.`agenda`;
CREATE TABLE  `mimsms`.`agenda` (
  `telefono` varchar(15) NOT NULL,
  `nombre` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`telefono`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mimsms`.`agenda`
--

/*!40000 ALTER TABLE `agenda` DISABLE KEYS */;
LOCK TABLES `agenda` WRITE;
INSERT INTO `mimsms`.`agenda` VALUES  ('04141933600','Luciano movistar'),
 ('04168933939','Luciano mobilnet');
UNLOCK TABLES;
/*!40000 ALTER TABLE `agenda` ENABLE KEYS */;


--
-- Definition of table `mimsms`.`contactos`
--

DROP TABLE IF EXISTS `mimsms`.`contactos`;
CREATE TABLE  `mimsms`.`contactos` (
  `telefono` varchar(15) NOT NULL,
  `nombre` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`telefono`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mimsms`.`contactos`
--

/*!40000 ALTER TABLE `contactos` DISABLE KEYS */;
LOCK TABLES `contactos` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `contactos` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
