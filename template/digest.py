import datetime
from core.badge import badgeGiver
from typing import List, Tuple, Any
import logging

def Digest(listOfNews: List[Tuple[str, str, str, Any]]) -> str:
    htmlContent: str = """
    <html>
    <body style="font-family: Arial, Helvetica, sans-serif; 
                background-color: #f4f6f8; 
                margin: 0; 
                padding: 30px; 
                text-align: center;
    ">
        <table role="presentation"
               cellspacing="0"
               cellpadding="0"
               border="0"
               align="center"
               width="100%" style="max-width: 650px;
               background: #ffffff;
               border-radius: 12px;
               box-shadow: 0 2px 10px rgba(0,0,0,0.08);
               overflow: hidden;
        ">
            <tr>
                <td style="padding: 30px 20px;
                           text-align: center;
                           border-bottom: 1px solid #eeeeee;
                ">
                    <h1 style="
                            margin: 0;
                            font-size: 50px;
                            color: #222222;
                            font-family:Georgia,serif
                    ">
                            Hacker News Daily Digest
                    </h1>
                    <p style="margin: 8px 0 0;
                              font-size: 15px;
                              color: #666666;
                              ">
                              Stay updated with the latest top stories
                    </p>
                </td>
            </tr>
            <tr>
                <td style="padding: 20px;">
    """
    try:
        sentTime: datetime.datetime = datetime.datetime.now()
        prettierSentTime: str = sentTime.strftime("%H:%M %p")
        giver: List[str] = badgeGiver()
        for (title, link, time, _), badge in zip(zip(*listOfNews), giver):
            badge = giver.pop(0) if badgeGiver else "🆕 Recent"
            htmlContent += f"""
                <div style='
                    background-color: #f9fafb;
                    padding: 16px 20px;
                    margin: 12px 0;
                    border-radius: 8px;
                    border: 1px solid #e5e7eb;
                    transition: all 0.2s ease-in-out;
                '>
                    <a href="{link}" style='
                        color: #2563eb;
                        text-decoration: none;
                        font-size: 16px;
                        font-weight: 500;
                        line-height: 1.4;
                        display: block;
                    '>{title}</a>
                    <span style="
                        color: #6b7280;
                        font-size: 10px;
                    ">
                        {time} - {badge}
                    </span>
                </div>
            """
        htmlContent += f"""
                    </td>
                </tr>
                <tr>
                    <td style="background: #f4f6f8;
                               padding: 20px;
                               text-align: center;
                               font-size: 13px;
                               color: #888888;
                    ">
                        {prettierSentTime}<br>
                    </td>                    
                </tr>
            </table>
        </body>
        </html>
        """
    except Exception as e:
        logging.error(f"Error generating digest: {e}")
        htmlContent = "<h1>Something is wrong... Please try again later.</h1>"
    return htmlContent
