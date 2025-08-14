const { ChatOpenAI } = require("@langchain/openai");
const { HumanMessage, SystemMessage } = require("@langchain/core/messages");

const optimizerHelper = async (resume, jobDescription) => {
    try{
        const workExperience = resume.workExperience;
        const description = jobDescription;
    
        const model = new ChatOpenAI({
            model: "gpt-4o-mini",
            temperature: 0,
          });

        // TODO: Implement actual AI optimization logic here
        // For now, return the original resume with a note
        console.log("Optimizing work experience for job description:", description);
        
        // Placeholder for AI optimization
        // const messages = [
        //     new SystemMessage("Translate the following from English into Italian"),
        //     new HumanMessage("hi!"),
        // ];
        
        // const response = await model.invoke(messages);
        // const optimizedExperience = JSON.parse(response.content);

        // For now, return the original resume
        return {
            ...resume,
            workExperience: workExperience // This would be optimized in the real implementation
        };
    }catch (error) {
        console.error("Error in optimizerHelper:", error);
        throw error;
    }
}


// @desc    Get the optimized resume
// @route   POST optimize
// @access  Private
const optimizeResume = async (req, res) => {
    try {
        const { resume, description } = req.body;
        if (!resume) {
            return res.status(400).json({ message: "Resume data is required" });
        }

        console.log("Optimizing resume for job description:", description);
    
        const optimizedResume = await optimizerHelper(resume, description);

        console.log("Resume optimization completed");
    
        res.json(optimizedResume);
    } catch (error) {
        console.error("Error in optimizeResume:", error);
        res
        .status(500)
        .json({ message: "Failed to optimize resume", error: error.message });
    }
  };

  module.exports = { optimizeResume };