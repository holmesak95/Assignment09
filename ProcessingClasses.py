#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# AHolmes, 2022-Mar-27, Updated ToDo logic
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.
        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """

        cdId, title, artist = CDInfo
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx
        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx
        """
        # TODONE add code as required
        intCD = 0
        for row_CD in table:
            if row_CD.cd_id == cd_idx:
                return row_CD
            intCD += 1
        print('There is no CD with that ID!')
        return None

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd
        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.
        """
        # TODONE add code as required
        objTrack = DC.Track(track_info[0], track_info[1], track_info[2])
        cd.add_track(objTrack)
    
    @staticmethod
    def select_track(cd: DC.CD, track_id: int) -> DC.Track:
        """
        Parameters
        ----------
        cd : DC.CD
            DESCRIPTION.
        track_id : int
            DESCRIPTION = the track id that the user wantss

        Returns
        -------
        row_track : TYPE
            DESCRIPTION = gets the track that user wants
        """
        
        # TODONE add code as required
        intTrackID = 0
        for row_track in cd.cd_tracks:
            if row_track.trk_position == track_id:
                return row_track
            intTrackID += 1
        print('There is no track with that ID!')
        return None

