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

        // const messages = [
        //     new SystemMessage("Translate the following from English into Italian"),
        //     new HumanMessage("hi!"),
        // ];
        
        // const response = await model.invoke(messages);

    
        return resume;
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
        return res.status(404).json({ message: "Resume not found or unauthorized" });
        }

        console.log("working");
    
        const optimizedResume = await optimizerHelper(resume, description);

        console.log("working 2");
    
        res.json(optimizedResume);
    } catch (error) {
        res
        .status(500)
        .json({ message: "Failed to create resume", error: error.message });
    }
  };

  module.exports = { optimizeResume };