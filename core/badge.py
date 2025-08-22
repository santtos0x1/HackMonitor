from core.inf_get import getNews
import logging

def badgeGiver() -> list:
    listOfNews = getNews()
    badges = []
    try:
        for _, _, time, score in zip(*listOfNews):
            timeValue = int(time.split()[0])
            scoreValue = int(score.split()[0])  # Extract the numeric part of the score
            if time.endswith("minutes ago"):
                timeValue /= 60 # Extract the numeric part of the time (in hours)
                
            if scoreValue > 0:
                scoreRatio = scoreValue / timeValue
                if scoreRatio >= 93:
                    badge = "🔥 Top News"
                elif scoreRatio >= 43:
                    badge = "⭐ Popular"
                elif scoreRatio >= 25:
                    badge = "📈 Trending"
                elif scoreRatio >= 19:
                    badge = "📊 Scalling"
                else:
                    badge = "🆕 Recent"
            else:
                badge = "Without Score"
            badges.append(badge)
    except ValueError:
        badge = "Without Score"
        logging.error("Error processing score or time values. Please check the data format.")
        
    return badges