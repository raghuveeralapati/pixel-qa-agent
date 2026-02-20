"""
Agent Module - Decision Engine
Maintainer: Raghuveer Alapati
"""

from utils.compare import compare_images

class ImageComparisonAgent:
    def __init__(self, threshold=95):
        self.threshold = threshold

    def analyze(self, img1, img2):
        similarity, diff = compare_images(img1, img2)

        if similarity >= self.threshold:
            decision = "Images are visually identical"
            status = "PASS"
        elif similarity >= 80:
            decision = "Minor visual differences detected"
            status = "WARNING"
        else:
            decision = "Significant differences detected"
            status = "FAIL"

        return {
            "similarity_score": f"{similarity:.2f}%",
            "decision": decision,
            "status": status
        }
