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

        
        //Placeholder for AI optimization
        const messages = [
            new SystemMessage(`You are a Resume Experience Optimizer. 
  Based on this Job Description: ${description}, identify key words and change the key words of each work experience in the the following work experience: ${JSON.stringify(workExperience, null, 2)} to best fit the jobdescription.
  keep the job title for each work experience and keep the essence of each job description but change the keys to best fit the job description,
  Key words include action verbs, technologies used, and skills required.
  Return the response as a list of JSON object with the format for each work experience:
  [{
    "jobTitle": "...",
    "optimizedExperience": ["line1", "line2", ...]
            }]
    
Also provide explain of what you changed        `
        
    ),
        ];
        
        const response = await model.invoke(messages);

        console.log(response.content)
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