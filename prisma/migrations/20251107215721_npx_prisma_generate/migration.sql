-- CreateTable
CREATE TABLE `ChatSession` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `userId` INTEGER NOT NULL,
    `title` VARCHAR(191) NOT NULL DEFAULT 'New Chat',
    `createdAt` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updatedAt` DATETIME(3) NOT NULL,

    INDEX `idx_user_sessions`(`userId`, `updatedAt` DESC),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `ChatMessage` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `sessionId` INTEGER NOT NULL,
    `userId` INTEGER NULL,
    `type` ENUM('user', 'assistant') NOT NULL,
    `content` LONGTEXT NOT NULL,
    `sources` JSON NULL,
    `createdAt` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),

    INDEX `idx_session_messages`(`sessionId`, `createdAt` ASC),
    INDEX `idx_message_user`(`userId`),
    INDEX `idx_message_createdAt`(`createdAt`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `FinanceAssessment` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `userId` INTEGER NOT NULL,
    `age` INTEGER NOT NULL,
    `gender` VARCHAR(191) NOT NULL,
    `educationLevel` VARCHAR(191) NOT NULL,
    `maritalStatus` VARCHAR(191) NOT NULL,
    `income` DOUBLE NOT NULL,
    `creditScore` DOUBLE NOT NULL,
    `loanAmount` DOUBLE NOT NULL,
    `loanPurpose` VARCHAR(191) NOT NULL,
    `employmentStatus` VARCHAR(191) NOT NULL,
    `yearsAtCurrentJob` INTEGER NOT NULL,
    `paymentHistory` VARCHAR(191) NOT NULL,
    `debtToIncomeRatio` DOUBLE NOT NULL,
    `assetsValue` DOUBLE NOT NULL,
    `numberOfDependents` DOUBLE NOT NULL,
    `previousDefaults` INTEGER NOT NULL,
    `maritalStatusChange` INTEGER NOT NULL,
    `riskRating` VARCHAR(191) NULL,
    `createdAt` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),

    INDEX `idx_finance_user`(`userId`),
    INDEX `idx_finance_created`(`createdAt`),
    INDEX `idx_finance_risk`(`riskRating`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `HealthAssessment` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `userId` INTEGER NOT NULL,
    `male` INTEGER NOT NULL,
    `age` INTEGER NOT NULL,
    `education` INTEGER NOT NULL,
    `currentSmoker` INTEGER NOT NULL,
    `cigsPerDay` DOUBLE NOT NULL,
    `bpMeds` INTEGER NOT NULL,
    `prevalentStroke` INTEGER NOT NULL,
    `prevalentHyp` INTEGER NOT NULL,
    `diabetes` INTEGER NOT NULL,
    `totChol` DOUBLE NOT NULL,
    `sysBP` DOUBLE NOT NULL,
    `diaBP` DOUBLE NOT NULL,
    `bmi` DOUBLE NOT NULL,
    `heartRate` DOUBLE NOT NULL,
    `glucose` DOUBLE NOT NULL,
    `tenYearCHD` INTEGER NULL,
    `probability` DOUBLE NULL,
    `createdAt` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),

    INDEX `idx_health_user`(`userId`),
    INDEX `idx_health_created`(`createdAt`),
    INDEX `idx_health_chd`(`tenYearCHD`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `ChatSession` ADD CONSTRAINT `ChatSession_userId_fkey` FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `ChatMessage` ADD CONSTRAINT `ChatMessage_sessionId_fkey` FOREIGN KEY (`sessionId`) REFERENCES `ChatSession`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `ChatMessage` ADD CONSTRAINT `ChatMessage_userId_fkey` FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FinanceAssessment` ADD CONSTRAINT `FinanceAssessment_userId_fkey` FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `HealthAssessment` ADD CONSTRAINT `HealthAssessment_userId_fkey` FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
