"""
Agentic Visual Validation AI Agent
Author: Raghuveer Alapati
Description: Intelligent pixel-to-pixel image comparison agent for QA and AI evaluation.
"""

from agent.image_agent import ImageComparisonAgent

if __name__ == "__main__":
    agent = ImageComparisonAgent(threshold=90)

    img1 = "samples/image1.png"
    img2 = "samples/image2.png"

    try:
        result = agent.analyze(img1, img2)
        print("🔍 AI Image Comparison Result")
        print("Similarity:", result["similarity_score"])
        print("Decision:", result["decision"])
        print("Status:", result["status"])
    except Exception as e:
        print("Error:", str(e))
