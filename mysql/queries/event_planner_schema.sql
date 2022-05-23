-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema event_planner_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `event_planner_schema` ;

-- -----------------------------------------------------
-- Schema event_planner_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `event_planner_schema` DEFAULT CHARACTER SET utf8 ;
USE `event_planner_schema` ;

-- -----------------------------------------------------
-- Table `event_planner_schema`.`events`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `event_planner_schema`.`events` ;

CREATE TABLE IF NOT EXISTS `event_planner_schema`.`events` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `event_title` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `location` VARCHAR(255) NULL,
  `start_time` DATETIME NULL,
  `end_time` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT 'NOW()',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`rsvp`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `event_planner_schema`.`rsvp` ;

CREATE TABLE IF NOT EXISTS `event_planner_schema`.`rsvp` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `responses` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `event_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_rsvp_events1_idx` (`event_id` ASC) VISIBLE,
  CONSTRAINT `fk_rsvp_events1`
    FOREIGN KEY (`event_id`)
    REFERENCES `event_planner_schema`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `event_planner_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `event_planner_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `event_id` INT NOT NULL,
  `rsvp_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_events_idx` (`event_id` ASC) VISIBLE,
  INDEX `fk_users_rsvp1_idx` (`rsvp_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_events`
    FOREIGN KEY (`event_id`)
    REFERENCES `event_planner_schema`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_rsvp1`
    FOREIGN KEY (`rsvp_id`)
    REFERENCES `event_planner_schema`.`rsvp` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
