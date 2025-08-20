const express = require("express");
const {
  createResume,
  getUserResumes,
  getResumeById,
  updateResume,
  deleteResume,
} = require("../controllers/resumeController");
const { optimizeResume } = require("../controllers/experienceOptimizer");
const { protect } = require("../middlewares/authMiddleware");
const { uploadResumeImages } = require("../controllers/uploadImages");

const router = express.Router();


router.post("/", protect, createResume);   // Create Resume
router.get("/", protect, getUserResumes);   // Get Resume
router.get("/:id", protect, getResumeById);   // Get Resume By ID
router.put("/:id", protect, updateResume);   // Update Resume
router.put("/:id/upload-images", protect, uploadResumeImages);
router.post("/:id/optimizedExperience", protect, optimizeResume);


router.delete("/:id", protect, deleteResume);   // Delete Resume

module.exports = router;